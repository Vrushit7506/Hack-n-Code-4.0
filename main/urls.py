from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('earth/', views.earth, name='earth'),
    path('child/', views.child, name='child'),
]
#
