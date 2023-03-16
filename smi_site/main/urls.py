from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main_page, name='main_page'),
    path('search/', views.SearchPage, name='search_page'),
    path('upload/', views.UploadPage, name='upload_page'),
    # path('upload/', views.UploadView.as_view(), name='fileupload'),
]
