from django.contrib import admin
from publication.models import Comment, Post
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'link_to_author', 'text', 'title', 'created_at', 'edited_at')
    list_filter = ('author', 'created_at',)
    search_fields = ('title', 'text')

    def link_to_author(self, obj):
        # Замените 'your_app_name' на название вашего приложения и 'related_object' на имя модели, на которую ссылается ваша связь
        change_url = reverse('admin:users_user_change', args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', change_url, obj.author)
    link_to_author.short_description = 'Автор'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created_at', 'edited_at')
    list_filter = ('author', 'created_at',)
    search_fields = ('id', 'author', 'post',)
