from django.urls import path
from .views import UserAPIView, GroupAPIView, DeviceAPIView

urlpatterns = [

    path('users/', UserAPIView.as_view(), name='users'),
    path('groups/', GroupAPIView.as_view(), name='groups'),
    path('devices/', DeviceAPIView.as_view(), name='devices'),

]