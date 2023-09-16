from django.db import models
from django.utils import timezone


class Category(models.Model):
    class Meta:
        verbose_name = "category"

    name = models.CharField("category_name", unique=True, max_length=20)

    created_at = models.DateTimeField("Created", editable=False, default=timezone.now)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Difficulty(models.Model):
    class Meta:
        verbose_name = "difficulty"

    name = models.CharField("difficulty_name", unique=True, max_length=20)
    point = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField("Created", editable=False, default=timezone.now)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Problem(models.Model):
    class Meta:
        verbose_name = "problem"

    title = models.CharField("problem_title", unique=True, max_length=20)
    content = models.TextField("problem_content")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField("Created", editable=False, default=timezone.now)
    updated_at = models.DateTimeField("Updated", default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
