from django.test import TestCase
from .models import *


class UrlTestCase(TestCase):

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.client.get('/mainpage/')
        self.assertEqual(response.status_code, 404)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    # def test_users(self):
    #     response = self.client.get('/users/login/')
    #     self.assertEqual(response.status_code, 200)

    def test_blog(self):
        response = self.client.get('/blog/articles/')
        self.assertEqual(response.status_code, 200)
