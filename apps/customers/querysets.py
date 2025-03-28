from django.db import models

class ServiceRequestQuerySet(models.QuerySet):
    def optimized_list(self):
        return self.select_related('customer').prefetch_related('attachments')

    def for_customer(self, user):
        return self.filter(customer=user)

    def with_attachments(self):
        return self.prefetch_related('attachments')