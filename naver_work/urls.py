from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.naver_work, name='naver_work'),

]
