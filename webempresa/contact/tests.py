from django.test import TestCase
from .forms import ContactForm

# Create your tests here.
class TestContact(TestCase):
    def setUp(self):
        self.data = {
            'name': 'Test User',
            'email': 'test@email.com',
            'content': 'Text content',
        }
        self.form = ContactForm(self.data)

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())
    def test_invalid_name(self):
        form = self.data.copy()
        form['name'] = ''
        form = ContactForm(form)
        self.assertFalse(form.is_valid())
    def test_invalid_email(self):
        form = self.data.copy()
        form['email'] = ''
        form = ContactForm(form)
        self.assertFalse(form.is_valid())
    def test_invalid_content(self):
        form = self.data.copy()
        form['content'] = ''
        form = ContactForm(form)
        self.assertFalse(form.is_valid())
