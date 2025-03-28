from django.db import models
from core.models import User
from core.validators import validate_file_type, validate_file_size

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('ESCALATED', 'Escalated'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status', 'priority']),
        ]

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

class RequestAttachment(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(
        upload_to='attachments/%Y/%m/%d/',
        validators=[validate_file_type, validate_file_size]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']