from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from main.models import Upload
from .serializers import UploadSerializer
 
class UploadListApiView(ListAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

