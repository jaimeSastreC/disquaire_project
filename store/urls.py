from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<album_id>\d+)/$', views.detail),
    url('search/', views.search, name ='search'),
]