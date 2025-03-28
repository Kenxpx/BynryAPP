from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('dashboard/', views.SupportDashboardView.as_view(), name='dashboard'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/update/', views.TicketUpdateView.as_view(), name='ticket_update'),
]