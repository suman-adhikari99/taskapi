from django.http import response
from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.user={
            'Email':"test@gmail.com",
            'Password':'test',
            'FirstName':'test',
            'LastName':'gmail'
        }

        return super().setUp()

class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'taskapp/regisration.html')

    def test_can_register_user(self):
        responser=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

