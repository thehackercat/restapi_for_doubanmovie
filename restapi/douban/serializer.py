#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from douban.models import Movies, celebrity, COUNTRY_CHOICES, TYPE_CHOICES

class MoviesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    director = serializers.CharField(source='celebrity.name')
    class Meta:
        model = Movies
        fields = ('id', 'title', 'director', 'year', 'country', 'type', 'rating', 'owner')

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movies.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')

class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movies.objects.all())

    class Meta:
        model = celebrity
        fields = ('id', 'name', 'age', 'gender', 'movies')
