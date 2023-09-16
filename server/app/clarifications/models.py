from problems.models import Problem

from django.db import models
from django.utils import timezone

from teams.models import Team


class Clarification(models.Model):
    class Meta:
        verbose_name = "clarification"

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    problem = models.ForeignKey(Problem, on_delete=models.SET_NULL, null=True)

    question = models.TextField()
    answer = models.TextField()
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField("Created", editable=False, default=timezone.now)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return f"{self.team.name}-{self.problem.title}"

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
