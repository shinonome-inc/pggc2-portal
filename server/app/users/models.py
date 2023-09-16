from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from teams.models import Team


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_data):
        email = self.normalize_email(f"{username}@example.com")
        user = self.model(self, username=username, email=email, **extra_data)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, password, **extra_data):
        extra_data.setdefault("is_staff", True)
        return self.create_user(username, password, **extra_data)

    def create_superuser(self, username, password, **extra_data):
        extra_data.setdefault("is_staff", True)
        extra_data.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_data)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "User"

    id = models.UUIDField("uuid", default=uuid4, primary_key=True, editable=False)
    username = models.CharField(
        "username",
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(1)],
        error_messages={"unique": "this username has been already used."},
    )

    email = models.EmailField(blank=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    is_staff = models.BooleanField(
        default=False,
        help_text="管理サイトにログインできるかを指定します。",
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self) -> str:
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
