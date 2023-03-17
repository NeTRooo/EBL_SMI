from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.UploadListApiView.as_view(), name='api_v1'),
]
