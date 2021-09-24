from django.urls import path
from .views import UserAPIView, GroupAPIView, DeviceAPIView, MemberAPIView

urlpatterns = [

    path('users/', UserAPIView.as_view(), name='users'),
    path('groups/', GroupAPIView.as_view(), name='groups'),
    path('members/', MemberAPIView.as_view(), name='members'),
    path('devices/', DeviceAPIView.as_view(), name='devices'),

]