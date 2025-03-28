from django.views.generic import TemplateView
from .dashboards import DashboardData

class AnalyticsDashboard(TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_data'] = DashboardData.status_distribution()
        context['priority_data'] = ServiceRequest.objects.values(
            'priority').annotate(count=Count('id'))
        return context