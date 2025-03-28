from celery import shared_task
from django.core.mail import send_mail
from .models import ServiceRequest

@shared_task
def notify_request_update(request_id):
    request = ServiceRequest.objects.get(id=request_id)
    subject = f"Request Update: {request.title}"
    message = f"Your request status has been updated to {request.status}"
    send_mail(
        subject,
        message,
        'noreply@gasutility.com',
        [request.customer.email],
        fail_silently=False,
    )

@shared_task
def process_attachments(request_id):
    from .models import RequestAttachment
    attachments = RequestAttachment.objects.filter(request_id=request_id)
    # Add custom attachment processing logic here