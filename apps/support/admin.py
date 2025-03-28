from django.contrib import admin
from .models import SupportTicket, SupportResponse

class SupportResponseInline(admin.StackedInline):
    model = SupportResponse
    extra = 1

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('request', 'assigned_to', 'status', 'created_at')
    list_filter = ('status', 'assigned_to')
    search_fields = ('request__title', 'request__description')
    inlines = [SupportResponseInline]

@admin.register(SupportResponse)
class SupportResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'staff', 'created_at')
    list_select_related = ('ticket', 'staff')