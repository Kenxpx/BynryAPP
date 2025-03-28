from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceRequest, RequestAttachment
from .forms import ServiceRequestForm

class RequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'customers/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.for_customer(
            self.request.user
        ).optimized_list()

class RequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'customers/request_create.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Request submitted successfully!')
        return response

    def get_success_url(self):
        return reverse_lazy('customers:request_detail', kwargs={'pk': self.object.pk})

class RequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'customers/request_detail.html'

    def get_queryset(self):
        return ServiceRequest.objects.for_customer(self.request.user)

class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'customers/request_update.html'

    def get_queryset(self):
        return ServiceRequest.objects.for_customer(self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Request updated successfully!')
        return super().form_valid(form)

class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRequest
    template_name = 'customers/request_confirm_delete.html'
    success_url = reverse_lazy('customers:request_list')

def add_attachment(request, pk):
    request_obj = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            RequestAttachment.objects.create(request=request_obj, file=file)
            messages.success(request, 'File attached successfully!')
        return redirect('customers:request_detail', pk=pk)
    return redirect('customers:request_detail', pk=pk)