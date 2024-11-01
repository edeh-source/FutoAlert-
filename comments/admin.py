from django.contrib import admin
from .models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created', 'active', 'updated']
    list_filter = ['author', 'post']