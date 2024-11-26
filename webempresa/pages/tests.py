from django.test import TestCase
from .models import Page

# Create your tests here.
class TestPage(TestCase):
    def setUp(self):
        self.page1 = Page.objects.create(
            title='Test Page',
            content='This is the content of the test page.',
            order=1
        )

    def test_create(self):
        self.assertEqual(Page.objects.count(), 1)
        self.assertEqual(self.page1.title, 'Test Page')
        self.assertEqual(self.page1.content, 'This is the content of the test page.')


    def test_order(self):
        self.page2 = Page.objects.create(
            title='Test Page 2',
            content='This is the content of the test page 2.',
            order=2
        )
        self.assertEqual(Page.objects.count(), 2)
        self.assertEqual(list(Page.objects.all()), [self.page1, self.page2])

    def test_str(self):
        self.assertEqual(str(self.page1), 'Test Page')

    def test_delete(self):
        self.page1.delete()
        self.assertEqual(Page.objects.count(), 0)
