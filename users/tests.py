from django.test import TestCase
from .models import *


class UrlTestCase(TestCase):

    def test_login(self):
        response = self.client.post('/users/login/', data={"username": "usertest",
                                                     "password": "passwordtest228336",
                                                     "email": "emailtest@gmail.com"})
        self.assertEqual(response.status_code, 200)

    def test_logup(self):
        test_logup_user = User.objects.create_user(username='testlogupusername',
                                 password="testloguppassword123123",
                                 email="testloguppassemail123123@gmail.com")
        test_logup_user.save()

        response = self.client.post('/users/register/', data={"username": "testlogupusername",
                                                     "password": "testloguppassword123123",
                                                     "email": "testloguppassemail123123@gmail.com"})
        self.assertEqual(response.status_code, 200)


