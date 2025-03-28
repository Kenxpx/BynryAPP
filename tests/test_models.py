from django.test import TestCase
from apps.core.models import User
from apps.customers.models import ServiceRequest

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email='test@user.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@user.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(user.user_type, 'CUSTOMER')

class ServiceRequestTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@user.com')
        self.request = ServiceRequest.objects.create(
            customer=self.user,
            title='Test Request',
            description='Test Description'
        )

    def test_request_creation(self):
        self.assertEqual(self.request.status, 'OPEN')
        self.assertEqual(str(self.request), 'Test Request - Open')