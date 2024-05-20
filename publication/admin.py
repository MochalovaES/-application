from django.contrib import admin
from publication.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'created_at', 'edited_at')
    list_filter = ('author', 'created_at',)
    #search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created_at', 'edited_at')
    list_filter = ('author', 'created_at',)
    #search_fields = ('id', 'author', 'ad',)
