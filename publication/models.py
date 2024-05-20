from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    """Создание модели объявления"""
    title = models.CharField(max_length=200, verbose_name='Заголовок поста')
    text = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста', **NULLABLE)
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Комментарий', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edited_at = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']  # Фильтрация по дате создания


class Comment(models.Model):
    """Создание модели отзыва"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва', **NULLABLE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст коммента')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edited_at = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']  # Фильтрация по дате создания
