from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_active', 'is_superuser', 'is_staff']
    list_filter = ['username', 'email', 'is_active', 'phone_number']
