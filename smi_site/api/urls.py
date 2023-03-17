from django.urls import path
from . import views

urlpatterns = [
    path('v1/all/', views.UploadListApiView.as_view(), name='api_all'),
    path('v1/tag/', views.UploadListCreateAPIView.as_view(), name='api_tag'),
]
