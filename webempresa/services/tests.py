from django.test import TestCase
from .models import Service

# Create your tests here.
class TestServices(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title="Test Service",
            subtitle="Test Subtitle",
            content="Test Content",
            image="services/test.jpg"
        )

    def test_create(self):
        self.assertEqual(self.service.title, "Test Service")
        self.assertEqual(self.service.subtitle, "Test Subtitle")
        self.assertEqual(self.service.content, "Test Content")
        self.assertEqual(self.service.image, "services/test.jpg")
    def test_service_str(self):
        self.assertEqual(str(self.service), "Test Service")

    def test_delete(self):
        self.service.delete()
        self.assertEqual(Service.objects.count(), 0)


