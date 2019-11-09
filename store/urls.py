from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

#distinguer par nespace de nom
app_name = 'store'

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<album_id>\d+)/$', views.detail, name="detail"),
    url('search/', views.search, name ='search'),
]