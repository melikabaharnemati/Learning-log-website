import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'learning_logs.settings'
import django
django.setup()

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Topic, Entry

class TopicTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')

        self.topic = Topic.objects.create(
            text='Test Topic', owner=self.user)

    def test_topic_text(self):
        """Test that the string representation of a topic is correct."""
        expected_result = 'Test Topic'
        self.assertEqual(str(self.topic), expected_result)

class EntryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')

        self.topic = Topic.objects.create(
            text='Test Topic', owner=self.user)

        self.entry = Entry.objects.create(
            topic=self.topic,
            text='Test Entry Text'
        )

    def test_entry_text(self):
        """Test that the string representation of an entry is correct."""
        expected_result = 'Test Entry Text...'
        self.assertEqual(str(self.entry), expected_result)

    def test_verbose_name_plural(self):
        """Test that the plural name of Entry model is correct."""
        expected_result = 'entries'
        self.assertEqual(Entry._meta.verbose_name_plural, expected_result)
