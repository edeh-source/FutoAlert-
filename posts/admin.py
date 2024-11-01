from django.contrib import admin
from .models import  Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated', 'active']
    list_filter = ['id', 'author', 'created', 'updated', 'active']