from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Hits

class TaskTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', password='pass')
        testuser1.save()

        test_hits = Hits.objects.create(
            added_by=testuser1,
            title='This is a title',
            description='This is a description'
        )
        test_hits.save()

    def test_hits_content(self):
        hits = Hits.objects.get(id=1)
        actual_owner = str(hits.added_by)
        actual_name = str(hits.title)
        actual_description = str(hits.description)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_name, 'This is a title')
        self.assertEqual(actual_description, 'This is a description')