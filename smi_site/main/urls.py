from django.db import router
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    # path('', views.main_page, name='main_page'),
    path('', views.test, name='test'),
    re_path('^search/(?P<search>.+)/$', views.SearchPageFilter, name='search_filter_page'),
    path('search/', views.SearchPage, name='search_page'),
    path('upload/', views.UploadPage, name='upload_page'),
    # path('upload/', views.UploadView.as_view(), name='fileupload'),
]
