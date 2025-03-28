from django.contrib import admin
from .models import User, Address

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', 'last_login')
    search_fields = ('email', 'phone')
    list_filter = ('user_type', 'is_active')
    ordering = ('-date_joined',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'is_primary')
    list_editable = ('is_primary',)
    search_fields = ('user__email', 'city')