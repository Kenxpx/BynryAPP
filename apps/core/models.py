from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('SUPPORT', 'Support Agent'),
        ('MANAGER', 'Manager'),
    )
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(
        max_length=10, 
        choices=USER_TYPE_CHOICES, 
        default='CUSTOMER'
    )
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['user_type']),
        ]

class Address(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='addresses'
    )
    street = models.CharField(_('street address'), max_length=255)
    city = models.CharField(_('city'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    postal_code = models.CharField(_('postal code'), max_length=20)
    is_primary = models.BooleanField(_('primary address'), default=False)
    
    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        unique_together = ('user', 'is_primary')
        
    def save(self, *args, **kwargs):
        if self.is_primary:
            Address.objects.filter(
                user=self.user, 
                is_primary=True
            ).update(is_primary=False)
        super().save(*args, **kwargs)