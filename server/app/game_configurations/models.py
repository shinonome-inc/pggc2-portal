from django.db import models
from django.utils import timezone


class Configuration(models.Model):
    class Meta:
        verbose_name = "configuration"

    field = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100, default="0")
    description = models.TextField()

    created_at = models.DateTimeField("Created", default=timezone.now, editable=False)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self):
        return self.field

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
