from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestURL(TestCase):
    def setUp(self):
        self.urls = ['home',
                     'about',
                     'services',
                     'store',
                     'contact',
                     'blog',
                     'sample']
    def test_url(self):
        for url_name in self.urls:
            url = reverse(url_name)  # URL para el nombre de la vista si existe en `urls.py`: /url/ .
            response = self.client.get(url)  # Método GET para la URL: simulación de solicitud HTTP.
            self.assertEqual(response.status_code, 200) # 200: código de respuesta HTTP de una solicitud exitosa.
