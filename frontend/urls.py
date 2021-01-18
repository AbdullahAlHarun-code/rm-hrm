from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('upload-cv', views.upload_cv, name="upload_cv"),
]
