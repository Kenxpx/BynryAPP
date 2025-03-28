from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'core/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if user.user_type == 'CUSTOMER':
            context['requests'] = user.requests.all()[:5]
        elif user.user_type in ['SUPPORT', 'MANAGER']:
            context['recent_tickets'] = SupportTicket.objects.filter(
                assigned_to=user
            )[:5]
        
        return context