from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import User

class CustomerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='customer@test.com',
            password='testpass123',
            user_type='CUSTOMER'
        )
        self.client.login(email='customer@test.com', password='testpass123')

    def test_request_list_view(self):
        response = self.client.get(reverse('customers:request_list'))
        self.assertEqual(response.status_code, 200)

class SupportViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='support@test.com',
            password='testpass123',
            user_type='SUPPORT'
        )
        self.client.login(email='support@test.com', password='testpass123')

    def test_dashboard_view(self):
        response = self.client.get(reverse('support:dashboard'))
        self.assertEqual(response.status_code, 200)