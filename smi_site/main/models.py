from django.db import models
from taggit.managers import TaggableManager

# upload_file, upload_date, link, tags
class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add=True)
    link = models.TextField(verbose_name='Ссылка на контент')
    tags = TaggableManager()
    
    class Meta:
        verbose_name = 'Ссылка на контент'
        verbose_name_plural = 'Ссылки на контент'
