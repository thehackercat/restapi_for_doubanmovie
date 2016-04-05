#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from douban import views

urlpatterns = [
    url(r'^dbmovies/$', views.MoviesList.as_view()),
    url(r'^dbmovies/(?P<pk>[0-9]+)/$', views.MoviesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)