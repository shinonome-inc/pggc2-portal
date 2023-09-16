from django.db import models
from django.utils import timezone


class TeamRole(models.Model):
    class Meta:
        verbose_name_plural = "Team Role"

    name = models.CharField("role", max_length=10, unique=True)

    created_at = models.DateTimeField("Created", editable=False, default=timezone.now)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Team(models.Model):
    class Meta:
        verbose_name_plural = "Teams"

    name = models.CharField("teamname", max_length=20, unique=True)
    role = models.ForeignKey(TeamRole, related_name="role", on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField("Created", default=timezone.now, editable=False)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
