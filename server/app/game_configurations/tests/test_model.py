from unittest import mock

from django.test import TestCase
from django.utils import timezone

from game_configurations.models import Configuration


class TestConfiguration(TestCase):
    def test_is_empty_configuration(self):
        self.assertEqual(Configuration.objects.all().count(), 0)

    def test_create_configuration(self):
        self.assertEqual(Configuration.objects.all().count(), 0)
        mock_date = timezone.datetime(2023, 1, 1)
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = mock_date
            config = Configuration.objects.create(field="test", value="0", description="test")
        self.assertEqual(Configuration.objects.all().count(), 1)
        self.assertEqual(str(config), config.field)
        self.assertEqual(config.field, "test")
        self.assertEqual(config.value, "0")
        self.assertEqual(config.description, "test")
        self.assertEqual(config.created_at, mock_date)
        self.assertEqual(config.updated_at, mock_date)
