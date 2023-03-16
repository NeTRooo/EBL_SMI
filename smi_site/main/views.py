from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
from django.contrib.auth.models import User, Group
from django import forms
from .models import Upload
from .forms import *
import datetime

def SearchPage(request):
    pass

def UploadPage(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            upload_file = form.cleaned_data['upload_file']
            m_tags = form.cleaned_data['m_tags']
            object = Upload(upload_file=upload_file)
            object.save()
            for m_tag in m_tags:
                object.tags.add(m_tag)
            form = UploadForm()
            return render(request, 'main/upload.html', {"form":form})
        else:
            form = UploadForm()
            return render(request, 'main/upload.html', {"form":form})
    else:
        form = UploadForm()
        return render(request, 'main/upload.html', {"form":form})

# class UploadView(CreateView):
#     model = Upload
#     fields = ['upload_file', ]
#     success_url = reverse_lazy('fileupload')
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['documents'] = Upload.objects.all()
#         return context