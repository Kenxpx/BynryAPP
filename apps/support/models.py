from django.db import models
from customers.models import ServiceRequest
from core.models import User

class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('ESCALATED', 'Escalated'),
    ]

    request = models.OneToOneField(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name='support_ticket'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tickets'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ('can_assign_ticket', 'Can assign support tickets'),
        ]

class SupportResponse(models.Model):
    ticket = models.ForeignKey(
        SupportTicket,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    internal = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']