from rest_framework import serializers

from publication.models import Comment, Post
from publication.validators import TitleValidator, AutorBirthDayValidator


class CommentSerializer(serializers.ModelSerializer):
    """"Класс-сериализатор для модели Comment"""

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Пост"""
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_birth_day = serializers.CharField(source="author.birth_day", read_only=True)

    # author_birth_day = serializers.DateField(validators=[AutorBirthDayValidator(field='autor.birth_day')])

    class Meta:
        model = Post
        fields = '__all__'
        validators = [AutorBirthDayValidator(field='autor.birth_day'),
                      TitleValidator(field='title')]
