from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomeViewTests(TestCase):

    def test_home_sucess(self):
        response = self.client.get(reverse('my-test-app:home'))

        self.assertEqual(response.status_code, 200)
