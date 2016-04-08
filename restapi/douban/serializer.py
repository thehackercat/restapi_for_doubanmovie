#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from douban.models import Movies, Director, COUNTRY_CHOICES, TYPE_CHOICES

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    director = serializers.HyperlinkedRelatedField(many=False, queryset=Director.objects.all(), view_name='director-detail')

    class Meta:
        model = Movies
        fields = ('url', 'title', 'director', 'year', 'country', 'type', 'rating', 'owner')

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, queryset=Movies.objects.all(), view_name='movies-detail',)

    class Meta:
        model = Director
        fields = ('url', 'name', 'age', 'gender', 'movies')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movies-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'movies')
