from django.contrib import admin

from .models import Status, Submission


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fieldsets = (("name", {"fields": ("name",)}),)
    list_display = ("name",)


@admin.register(Submission)
class SubmissioAdmin(admin.ModelAdmin):
    fieldsets = (
        ("team", {"fields": ("team",)}),
        ("problem", {"fields": ("problem",)}),
        ("info", {"fields": ("status", "score")}),
    )
    list_display = ("team", "problem", "status", "score")
