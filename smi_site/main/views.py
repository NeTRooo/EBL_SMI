from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.contrib.auth.models import User, Group
from django import forms
from .models import Upload
from .forms import *
import datetime

def SearchPage(request):
    return render(request, 'main/search.html')


def SearchPageFilter(request, search):
    response = requests.get(f'http://localhost:8000/api/v1/tag?search={search}')
    if response.json() == []:
        return render(request, 'main/search.html')
    else:
        return render(request, 'main/search_filter.html', {"content": response.json()})

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
