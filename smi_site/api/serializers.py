from rest_framework import serializers
from main.models import Upload
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

# upload_file, upload_date, link, tags
class UploadSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = Upload
        fields = ('upload_file', 'upload_date', 'tags')