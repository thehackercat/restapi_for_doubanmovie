#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from douban.models import Movies, COUNTRY_CHOICES, TYPE_CHOICES

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'title', 'year', 'country', 'type', 'rating')