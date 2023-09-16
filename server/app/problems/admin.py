from django.contrib import admin

from .models import Category, Difficulty, Problem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (("name", {"fields": ("name",)}),)
    list_display = ("name",)


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    fieldsets = (("name", {"fields": ("name",)}), ("point", {"fields": ("point",)}))
    list_display = ("name", "point")


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    fieldsets = (
        ("title", {"fields": ("title",)}),
        ("content", {"fields": ("content",)}),
        ("category", {"fields": ("category",)}),
        ("difficulty", {"fields": ("difficulty",)}),
    )
    list_display = ("title", "category", "difficulty")
