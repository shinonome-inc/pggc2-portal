from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username",)}),
        ("Team", {"fields": ("team",)}),
        ("個人情報", {"fields": ("email", "password")}),
    )
    list_display = ("username", "team", "is_staff")
    search_fields = ("username",)
