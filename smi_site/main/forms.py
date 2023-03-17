from django import forms
from taggit.forms import *

class UploadForm(forms.Form):
    upload_file = forms.FileField(label='Выберите файл')
    m_tags = TagField()

class SearchForm(forms.Form):
    search = forms.CharField(label='Тег для поиска', max_length=128)