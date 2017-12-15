from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.naver_work, name='naver_work'),
    path('post/<int:pk>/detail/test', views.test, name='test'),

    path('task', views.task, name='task'),

    path('idlist', views.idlist, name='idlist'),
    path('idlist/add', views.idlist_add, name='idlist_add'),

    path('cafelist', views.cafelist, name='cafelist'),
    path('cafelist/add', views.cafelist_add, name='cafelist_add'),
    path('cafelist/<int:pk>/edit', views.cafelist_edit, name='cafelist_edit'),

    path('postlist', views.postlist, name='postlist'),
    path('post/add', views.post_add, name='post_add'),
    path('post/<int:pk>/detail', views.post_detail, name='post_detail'),
    path('post/<int:pk>/detail/edit', views.post_edit, name='post_edit'),

]
