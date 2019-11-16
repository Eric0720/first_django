#!/usr/bin/env python
#encoding:utf-8
__author__ = 'eric'

from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {'title': 'This is Title', 'message': 'This is message'})
