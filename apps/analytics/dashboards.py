from django.db.models import Count, Case, When, IntegerField
from customers.models import ServiceRequest

def get_request_analytics():
    return ServiceRequest.objects.aggregate(
        total_requests=Count('id'),
        open_requests=Count(Case(When(status='OPEN', then=1))),
        avg_resolution_time=Avg(F('resolved_at') - F('created_at'))
    )

class DashboardData:
    @classmethod
    def status_distribution(cls):
        return ServiceRequest.objects.values('status').annotate(
            count=Count('id'),
            percentage=ExpressionWrapper(
                Count('id') * 100.0 / ServiceRequest.objects.count(),
                output_field=FloatField()
            )
        )