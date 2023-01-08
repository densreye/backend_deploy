
from django.urls import path, include

from web import viewsplan
from . import views

from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "web"

urlpatterns = [


    path('', views.index, name = "index"),

    
]
urlpatterns = format_suffix_patterns(urlpatterns)