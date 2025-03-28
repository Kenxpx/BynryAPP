from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('requests/', views.RequestListView.as_view(), name='request_list'),
    path('requests/create/', views.RequestCreateView.as_view(), name='request_create'),
    path('requests/<int:pk>/', views.RequestDetailView.as_view(), name='request_detail'),
    path('requests/<int:pk>/update/', views.RequestUpdateView.as_view(), name='request_update'),
    path('requests/<int:pk>/delete/', views.RequestDeleteView.as_view(), name='request_delete'),
    path('requests/<int:pk>/attach/', views.add_attachment, name='add_attachment'),
]