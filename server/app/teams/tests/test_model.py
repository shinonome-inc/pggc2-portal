from unittest import mock

from django.test import TestCase
from django.utils import timezone

from teams.models import Team, TeamRole


class TestTeamRoleModel(TestCase):
    def test_is_empty_team_role(self):
        self.assertEqual(TeamRole.objects.all().count(), 0)

    def test_create_team_role(self):
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            team_role = TeamRole.objects.create(name="test")
        self.assertEqual(TeamRole.objects.all().count(), 1)
        self.assertEqual(str(team_role), team_role.name)
        self.assertEqual(team_role.name, "test")
        self.assertEqual(team_role.created_at, mock_date)
        self.assertEqual(team_role.updated_at, mock_date)

    def test_update_team_role(self):
        team_role = TeamRole.objects.create(name="test")
        team_role.name = "test2"
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            team_role.save()
        self.assertEqual(team_role.name, "test2")
        self.assertEqual(team_role.updated_at, mock_date)

    def test_delete_team_role(self):
        team_role = TeamRole.objects.create(name="test")
        self.assertEqual(TeamRole.objects.all().count(), 1)
        team_role.delete()
        self.assertEqual(TeamRole.objects.all().count(), 0)


class TestTeamModel(TestCase):
    def setUp(self):
        self.contestant = TeamRole.objects.create(name="Contestant")
        self.admin = TeamRole.objects.create(name="Admin")
        return super().setUp()

    def test_is_empty_team(self):
        self.assertEqual(Team.objects.all().count(), 0)

    def test_create_team(self):
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            team = Team.objects.create(name="test", role=self.contestant)
        all_teams = Team.objects.all()
        self.assertEqual(all_teams.count(), 1)
        self.assertEqual(str(team), team.name)
        self.assertEqual(team.name, "test")
        self.assertEqual(team.role, self.contestant)
        self.assertEqual(team.created_at, mock_date)
        self.assertEqual(team.updated_at, mock_date)

    def test_update_team_name(self):
        team = Team.objects.create(name="test", role=self.contestant)
        team.name = "test2"
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            team.save()
        self.assertEqual(team.name, "test2")
        self.assertEqual(team.updated_at, mock_date)

    def test_update_team_role(self):
        team = Team.objects.create(name="test", role=self.contestant)
        self.assertEqual(team.role, self.contestant)
        team.role = self.admin
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            team.save()
        self.assertEqual(team.role, self.admin)
        self.assertEqual(team.role.name, self.admin.name)
        self.assertEqual(team.updated_at, mock_date)

    def test_delete_team(self):
        team = Team.objects.create(name="test", role=self.contestant)
        self.assertEqual(Team.objects.all().count(), 1)
        team.delete()
        self.assertEqual(Team.objects.all().count(), 0)
