from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from publication.models import Comment, Post
from publication.serializers import CommentSerializer, PostSerializer
from users.permissions import IsOwner, IsAdmin


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """Создавать и просматривать может любой авторизованный пользователь, а редактировать
        и удалять только владелец или админ"""
        permission_classes = []
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Автоматическое сохранение владельца при создании объекта"""
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получает отзывы для определенного поста"""
        return self.queryset.filter(post=self.kwargs['post_pk'])

    def get_permissions(self):
        """Создавать и просматривать может любой авторизованный пользователь, а редактировать
        и удалять только владелец или админ"""
        permission_classes = []
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Автоматическое сохранение владельца отзыва в определенном посте"""
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.post = Post.objects.get(pk=self.kwargs['post_pk'])
        new_comment.save()
