from django.contrib import admin

from .models import Team, TeamRole


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    fieldsets = (("name", {"fields": ("name",)}),)
    list_display = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "info",
            {"fields": ("name", "role")},
        ),
    )
    list_display = ("name",)
    search_display = ("name",)
