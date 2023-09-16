from unittest import mock

from problems.models import Problem

from django.test import TestCase
from django.utils import timezone

from clarifications.models import Clarification
from teams.models import Team


class TestClarification(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="test")
        self.problem = Problem.objects.create(title="test")
        return super().setUp()

    def test_is_empty_clarificaton(self):
        self.assertEqual(Clarification.objects.all().count(), 0)

    def test_create_clarificaton(self):
        self.assertEqual(Clarification.objects.all().count(), 0)
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            clar = Clarification.objects.create(
                team=self.team, problem=self.problem, question="testquestion", answer="testanswer"
            )
        self.assertEqual(Clarification.objects.all().count(), 1)
        self.assertEqual(str(clar), f"{self.team.name}-{self.problem.title}")
        self.assertEqual(clar.team, self.team)
        self.assertEqual(clar.problem, self.problem)
        self.assertEqual(clar.question, "testquestion")
        self.assertEqual(clar.answer, "testanswer")
        self.assertEqual(clar.created_at, mock_date)
        self.assertEqual(clar.updated_at, mock_date)
