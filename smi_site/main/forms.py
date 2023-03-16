from django import forms
from taggit.forms import *

class UploadForm(forms.Form):
    upload_file = forms.FileField(label='Select a file')
    m_tags = TagField()