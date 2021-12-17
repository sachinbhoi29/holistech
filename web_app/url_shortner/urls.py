from django.contrib import admin
from django.urls import path
from url_shortner import views


urlpatterns = [
    path("",views.url_shortner, name='home'),
]