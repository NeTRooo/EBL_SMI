from rest_framework import viewsets
from rest_framework.generics import ListAPIView, ListCreateAPIView
from main.models import Upload
from .serializers import UploadSerializer
from rest_framework import filters
 
class UploadListApiView(ListAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

class UploadListCreateAPIView(ListCreateAPIView):
    search_fields = ['tags__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
