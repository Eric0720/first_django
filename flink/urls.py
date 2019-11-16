#!/usr/bin/env python
#encoding:utf-8
__author__ = 'eric'

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]