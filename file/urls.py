from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download')
]