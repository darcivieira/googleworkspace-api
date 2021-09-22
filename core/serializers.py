from rest_framework import serializers, fields
from .models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditLog
        fields = (
            'created',
            'user_id',
            'access_type',
            'api_url',
            'api_options'
        )