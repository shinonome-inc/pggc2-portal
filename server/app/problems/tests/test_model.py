from unittest import mock

from problems.models import Category, Difficulty, Problem

from django.test import TestCase
from django.utils import timezone


class TestCategory(TestCase):
    def test_is_empty_category(self):
        self.assertEqual(Category.objects.all().count(), 0)

    def test_create_category(self):
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            category = Category.objects.create(name="test")
        self.assertEqual(Category.objects.all().count(), 1)
        self.assertEqual(str(category), category.name)
        self.assertEqual(category.name, "test")
        self.assertEqual(category.created_at, mock_date)
        self.assertEqual(category.updated_at, mock_date)

    def test_update_category(self):
        category = Category.objects.create(name="test")
        category.name = "test2"
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            category.save()
        self.assertEqual(category.name, "test2")
        self.assertEqual(category.updated_at, mock_date)

    def test_delete_category(self):
        category = Category.objects.create(name="test")
        self.assertEqual(Category.objects.all().count(), 1)
        category.delete()
        self.assertEqual(Category.objects.all().count(), 0)


class TestDifficulty(TestCase):
    def test_is_empty_difficulty(self):
        self.assertEqual(Difficulty.objects.all().count(), 0)

    def test_create_difficulty(self):
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            difficulty = Difficulty.objects.create(name="test", point=2)
        self.assertEqual(Difficulty.objects.all().count(), 1)
        self.assertEqual(str(difficulty), difficulty.name)
        self.assertEqual(difficulty.name, "test")
        self.assertEqual(difficulty.point, 2)
        self.assertEqual(difficulty.created_at, mock_date)
        self.assertEqual(difficulty.updated_at, mock_date)

    def test_update_difficulty_name(self):
        difficulty = Difficulty.objects.create(name="test")
        difficulty.name = "test2"
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            difficulty.save()
        self.assertEqual(difficulty.name, "test2")
        self.assertEqual(difficulty.updated_at, mock_date)

    def test_update_difficulty_point(self):
        difficulty = Difficulty.objects.create(name="test", point=0)
        difficulty.point = 2
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            difficulty.save()
        self.assertEqual(difficulty.point, 2)
        self.assertEqual(difficulty.updated_at, mock_date)

    def test_delete_difficulty(self):
        difficulty = Difficulty.objects.create(name="test")
        self.assertEqual(Difficulty.objects.all().count(), 1)
        difficulty.delete()
        self.assertEqual(Difficulty.objects.all().count(), 0)


class TestProblem(TestCase):
    def setUp(self) -> None:
        self.cat1 = Category.objects.create(name="cat1")
        self.cat2 = Category.objects.create(name="cat2")
        self.diff1 = Difficulty.objects.create(name="diff1")
        self.diff2 = Difficulty.objects.create(name="diff2")
        return super().setUp()

    def test_create_problem(self):
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            problem = Problem.objects.create(title="test", content="", category=self.cat1, difficulty=self.diff1)
        self.assertEqual(Problem.objects.all().count(), 1)
        self.assertEqual(str(problem), problem.title)
        self.assertEqual(problem.title, "test")
        self.assertEqual(problem.content, "")
        self.assertEqual(problem.category, self.cat1)
        self.assertEqual(problem.difficulty, self.diff1)

    def test_update_problem_title(self):
        problem = Problem.objects.create(title="test", category=self.cat1, difficulty=self.diff1)
        problem.title = "test2"
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            problem.save()
        self.assertEqual(problem.title, "test2")
        self.assertEqual(problem.updated_at, mock_date)

    def test_update_problem_category(self):
        problem = Problem.objects.create(title="test", category=self.cat1, difficulty=self.diff1)
        problem.category = self.cat2
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            problem.save()
        self.assertEqual(problem.category, self.cat2)
        self.assertEqual(problem.updated_at, mock_date)

    def test_update_problem_difficulty(self):
        problem = Problem.objects.create(title="test", category=self.cat1, difficulty=self.diff1)
        problem.difficulty = self.diff2
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            problem.save()
        self.assertEqual(problem.difficulty, self.diff2)
        self.assertEqual(problem.updated_at, mock_date)

    def test_delete_problem(self):
        problem = Problem.objects.create(title="test", category=self.cat1, difficulty=self.diff1)
        self.assertEqual(Problem.objects.all().count(), 1)
        problem.delete()
        self.assertEqual(Problem.objects.all().count(), 0)
