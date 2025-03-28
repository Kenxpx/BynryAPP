from django.contrib import admin
from .models import ServiceRequest, RequestAttachment

class RequestAttachmentInline(admin.TabularInline):
    model = RequestAttachment
    extra = 1

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description', 'customer__email')
    inlines = [RequestAttachmentInline]
    date_hierarchy = 'created_at'

@admin.register(RequestAttachment)
class RequestAttachmentAdmin(admin.ModelAdmin):
    list_display = ('request', 'file', 'uploaded_at')
    list_select_related = ('request',)