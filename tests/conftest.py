import pytest
from django.contrib.auth.models import User
from apps.customers.models import ServiceRequest

@pytest.fixture
def customer_user(db):
    return User.objects.create_user(
        email='customer@test.com',
        password='testpass123',
        user_type='CUSTOMER'
    )

@pytest.fixture
def support_user(db):
    return User.objects.create_user(
        email='support@test.com',
        password='testpass123',
        user_type='SUPPORT'
    )

@pytest.fixture
def service_request(customer_user):
    return ServiceRequest.objects.create(
        customer=customer_user,
        title='Test Request',
        description='Test Description',
        status='OPEN'
    )