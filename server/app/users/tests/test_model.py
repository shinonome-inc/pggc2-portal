from django.test import TestCase

from teams.models import Team, TeamRole
from users.models import User


class TestUser(TestCase):
    def setUp(self) -> None:
        role = TeamRole.objects.create(name="test_role")
        self.team1 = Team.objects.create(name="test_team", role=role)
        self.team2 = Team.objects.create(name="test_team2", role=role)
        return super().setUp()

    def test_is_empty_user(self):
        self.assertEqual(User.objects.all().count(), 0)

    def test_create_user(self):
        self.assertEqual(User.objects.all().count(), 0)
        user = User.objects.create(username="test", email="test@example.com", password="testuser0123", team=self.team1)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(str(user), user.username)
        self.assertEqual(user.get_full_name(), user.username)
        self.assertEqual(user.get_short_name(), user.username)
        self.assertEqual(user.username, "test")
        self.assertEqual(user.team, self.team1)

    def test_user_manager(self):
        user = User.objects.create_user(username="test01", password="test0123")  # type: ignore
        self.assertEqual(user.username, "test01")
        self.assertEqual(user.email, "test01@example.com")
        staff_user = User.objects.create_staff(username="staff", password="test0123")  # type: ignore
        self.assertEqual(staff_user.username, "staff")
        self.assertEqual(staff_user.email, "staff@example.com")
        super_user = User.objects.create_superuser(username="admin", password="test0123")  # type: ignore
        self.assertEqual(super_user.username, "admin")
        self.assertEqual(super_user.email, "admin@example.com")

    def test_switch_team(self):
        user = User.objects.create(username="test", email="test@example.com", password="testuser0123", team=self.team1)
        self.assertEqual(user.team, self.team1)
        user.team = self.team2
        user.save()
        self.assertEqual(user.team, self.team2)

    def test_delete_user(self):
        user = user = User.objects.create(
            username="test", email="test@example.com", password="testuser0123", team=self.team1
        )
        self.assertEqual(User.objects.all().count(), 1)
        user.delete()
        self.assertEqual(User.objects.all().count(), 0)
