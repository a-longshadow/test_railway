from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'published']
    list_filter = ['created_at', 'updated_at', 'published', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['content', 'author__username']
    raw_id_fields = ['post', 'author']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
