from rest_framework import serializers

from publication.models import Comment, Post
from publication.validators import TitleValidator
from datetime import date


class CommentSerializer(serializers.ModelSerializer):
    """"Класс-сериализатор для модели Comment"""

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Пост"""
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_birth_day = serializers.CharField(source="author.birth_day", read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        validators = [TitleValidator(field='title')]

    def validate(self, data):
        author = self.instance.author if self.instance else self.context['request'].user
        birth_day = author.birth_day
        age = (date.today() - birth_day).days // 365
        if age < 18:
            raise serializers.ValidationError({'author': 'Автор поста не достиг возраста 18 лет.'})
        return data
