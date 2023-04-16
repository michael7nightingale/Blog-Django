import http
import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.


class BlogAppTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(BlogAppTest, cls).setUpClass()
        django.setup()

    def test_access1(self):
        response = self.client.get('/blog/articles/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_access2(self):
        self.client.login(username='admin', password='password')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
