#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from douban import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^movies/$', views.MoviesList.as_view(), name='movies-list'),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MoviesDetail.as_view(), name='movies-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^directors/$', views.DirectorList.as_view(), name='director-list'),
    url(r'^directors/(?P<pk>[0-9]+)/$', views.DirectorDetail.as_view(), name='director-detail'),
])
