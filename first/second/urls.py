from django.urls import path
from second import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.helloWorld),
    path('user/<int:id>/', views.userById),
    path('all-users/', views.allUsers),
]