from unittest import mock

from problems.models import Problem

from django.test import TestCase
from django.utils import timezone

from submissions.models import Status, Submission
from teams.models import Team


class TestStatus(TestCase):
    def test_is_empty_status(self):
        self.assertEqual(Status.objects.all().count(), 0)

    def test_create_status(self):
        self.assertEqual(Status.objects.all().count(), 0)
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            status = Status.objects.create(name="test")
        self.assertEqual(Status.objects.all().count(), 1)
        self.assertEqual(str(status), status.name)
        self.assertEqual(status.name, "test")
        self.assertEqual(status.created_at, mock_date)
        self.assertEqual(status.updated_at, mock_date)


class TestSubmission(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="test")
        self.problem = Problem.objects.create(title="test")
        self.status = Status.objects.create(name="correct")
        return super().setUp()

    def test_is_empty_submission(self):
        self.assertEqual(Submission.objects.all().count(), 0)

    def test_create_submission(self):
        self.assertEqual(Submission.objects.all().count(), 0)
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            submission = Submission.objects.create(team=self.team, problem=self.problem, status=self.status, score=0)
        self.assertEqual(Submission.objects.all().count(), 1)
        self.assertEqual(str(submission), f"{self.team.name}-{self.problem.title}")
        self.assertEqual(submission.team, self.team)
        self.assertEqual(submission.problem, self.problem)
        self.assertEqual(submission.status, self.status)
        self.assertEqual(submission.score, 0)
        self.assertEqual(submission.created_at, mock_date)
        self.assertEqual(submission.updated_at, mock_date)
