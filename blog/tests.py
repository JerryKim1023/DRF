from django.test import TestCase
from blog.models import Article, Category

from blog.services import create_article

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from user.models import User

# Create your tests here.

class TestView(TestCase):
    """ C R E A T E """

    def test_create_article(self):
        # Given
        user = User.objects.create(username='test_name', email='test@test.com')
        title = 'test_title'
        content = 'content'
        category = Category.objects.create(name='test_category')

        # When
        article = create_article(title, user, content, category)

        # expect
        self.assertIsNotNone(Article.id)
        self.assertEqual(user.id, article.user.id)