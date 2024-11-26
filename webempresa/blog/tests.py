from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post
from django.utils import timezone
from unittest.mock import MagicMock
import os
from django.core.files import File

# Create your tests here.
class TestCategory(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category'
        )

    def test_create(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(self.category.name, 'Test Category')

    def test_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_delete(self):
        self.category.delete()
        self.assertEqual(Category.objects.count(), 0)



class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is the content of the test post.',
            published=timezone.now(),
            author=self.user
        )
        self.post.categories.add(self.category)

    def test_create(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is the content of the test post.')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.categories.count(), 1)
        self.assertEqual(self.post.categories.first().name, 'Test Category')

    def test_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_order(self):
        post2 = Post.objects.create(
            title='Test Post 2',
            content='This is another test post.',
            published=timezone.now(),
            author=self.user
        )
        post2.categories.add(self.category)
        posts = list(Post.objects.all())
        self.assertEqual(posts[1], post2)
        self.assertEqual(posts[0], self.post)
        post2.delete()

    def test_image_upload(self):
        image_path = 'test_image.jpg'
        mock_file = MagicMock(spec=File)
        mock_file.name = image_path
        self.post.image.save(image_path, mock_file)

        self.assertTrue(os.path.exists(self.post.image.path))
        self.assertTrue(self.post.image.name.endswith(image_path))

        self.post.image.delete()

    def test_delete(self):
        self.post.delete()
        self.assertEqual(Post.objects.count(), 0)

    def test_author_deleted(self):
        self.user.delete()
        self.assertEqual(Post.objects.count(), 0)
