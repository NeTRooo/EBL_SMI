from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main_page, name='main_page'),
    # path('search/', views.search_page, name='search_page'),
    # path('upload/', views.upload_page, name='upload_page'),
    path('upload/', views.UploadView.as_view(), name='fileupload'),
]
