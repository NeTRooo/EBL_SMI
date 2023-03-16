from django.contrib import admin
from .models import Upload

#  
#  configuring the display
#  

# upload_file, upload_date, link, tags
class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_file', 'upload_date')
    list_display_links = ('upload_file', 'upload_date')
    search_fields = ('upload_file', 'upload_date')

#  
#  Register model
#  

admin.site.register(Upload, UploadAdmin)