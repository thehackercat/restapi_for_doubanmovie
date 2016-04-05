#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# 举个栗子
COUNTRY_CHOICES = (
    ('US', 'US'),
    ('Asia', 'Asia'),
    ('CN', 'CN'),
    ('TW', 'TW'),
)
TYPE_CHOICES = (
    ('Drama', 'Drama'),
    ('Thriller', 'Thriller'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Romance', 'Romance'),
    ('Comedy', 'Comedy')
)
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female')
)

class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year = models.CharField(max_length=20)
    # 在 director 关联了 movies 类 和 celecrity 类, 在第4章会用到 celebrity 类
    # director = models.ForeignKey('celebrity', related_name='movies')
    country = models.CharField(choices=COUNTRY_CHOICES, default='US', max_length=20)
    type = models.CharField(choices=TYPE_CHOICES, default='Romance', max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

# class celebrity(models.Model):
#     name = models.CharField(max_length=100, blank=True, default='')
#     age = models.IntegerField()
#     gender = models.CharField(choices=GENDER_CHOICES, default='男', max_length=20)