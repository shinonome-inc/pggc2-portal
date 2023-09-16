from django.contrib import admin

from .models import Clarification


@admin.register(Clarification)
class ClarificationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("from", {"fields": ("team",)}),
        ("about", {"fields": ("problem",)}),
        ("qa", {"fields": ("question", "answer")}),
        ("public", {"fields": ("is_public",)}),
    )
    list_display = ("team", "problem", "is_public")
