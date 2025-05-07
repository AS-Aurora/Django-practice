from django.urls import path
from second import views
from django.contrib import admin

urlpatterns = [
    path('helloworld/', views.helloworld)
]