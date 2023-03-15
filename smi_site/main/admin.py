from django.contrib import admin
from .models import Upload, ContentLinks

#  
#  configuring the display
#  

# upload_file, upload_date
class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_file', 'upload_date')
    list_display_links = ('upload_file', 'upload_date')
    search_fields = ('upload_file', 'upload_date')

# upload, link
class ContentLinksAdmin(admin.ModelAdmin):
    list_display = ('link',)
    list_display_links = ('link',)
    search_fields = ('link',)

#  
#  Register model
#  

admin.site.register(Upload, UploadAdmin)
admin.site.register(ContentLinks, ContentLinksAdmin)