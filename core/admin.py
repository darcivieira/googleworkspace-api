from django.contrib import admin

from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'user_id',
        'access_type',
        'api_url',
        'api_options'
    )
