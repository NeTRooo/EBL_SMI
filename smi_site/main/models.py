from django.db import models
from taggit.managers import TaggableManager

class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)

class ContentLinks(models.Model):
    upload = models.OneToOneField(Upload, on_delete=models.CASCADE, verbose_name='Линки к контенту')
    link = models.TextField(verbose_name='Ссылка на контент')
    tags = TaggableManager()
    
    class Meta:
        verbose_name = 'Ссылка на контент'
        verbose_name_plural = 'Ссылки на контент'
