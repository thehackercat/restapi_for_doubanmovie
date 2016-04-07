#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from douban.permissions import IsOwnerOrReadOnly
from douban.models import Movies, celebrity
from douban.serializer import MoviesSerializer, UserSerializer, DirectorSerializer
from rest_framework import generics
from rest_framework import permissions

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, director=self.request.celebrity)

class MoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, director=self.request.celebrity)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DirectorList(generics.ListCreateAPIView):
    queryset = celebrity.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = celebrity.objects.all()
    serializer_class = DirectorSerializer