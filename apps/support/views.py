from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import SupportTicket
from .forms import SupportTicketForm

class SupportDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = SupportTicket
    template_name = 'support/dashboard.html'
    context_object_name = 'tickets'

    def test_func(self):
        return self.request.user.user_type in ['SUPPORT', 'MANAGER']

    def get_queryset(self):
        return SupportTicket.objects.select_related(
            'request', 'assigned_to'
        ).order_by('-created_at')

class TicketDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = SupportTicket
    template_name = 'support/ticket_detail.html'

    def test_func(self):
        return self.request.user.user_type in ['SUPPORT', 'MANAGER']

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'support/ticket_update.html'

    def test_func(self):
        return self.request.user.user_type in ['SUPPORT', 'MANAGER']

    def form_valid(self, form):
        messages.success(self.request, 'Ticket updated successfully!')
        return super().form_valid(form)