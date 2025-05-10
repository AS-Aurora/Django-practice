from django.urls import path
from     second import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.helloWorld, name='home'),
    path('user/<int:id>/', views.userById, name='user-profile'),
    path('all-users/', views.allUsers),
    path('all-users/redirect-to-<int:id>/', views.redirectToUser, name='redirect-to-user'),
    # path('userName/<int:id>/', views.userName)
]