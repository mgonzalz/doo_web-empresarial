from django.test import TestCase
from .models import Link

# Create your tests here.
class TestLink(TestCase):
    def setUp(self):
        self.link = Link.objects.create(
            key='facebook',
            name='Facebook',
            url='https://www.facebook.com'
        )

    def test_social(self):
        self.assertEqual(self.link.key, 'facebook')
        self.assertEqual(self.link.name, 'Facebook')
        self.assertEqual(self.link.url, 'https://www.facebook.com')
        self.assertEqual(str(self.link), 'Facebook')
    
    def test_str(self):
        self.assertEqual(str(self.link), 'Facebook')
