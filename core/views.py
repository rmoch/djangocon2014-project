# -*- coding: utf-8 -*-

from django.shortcuts import render

def index(request):

    return render(request, 'core/index.html', {
        'active': 'index',
            })

def ais(request):

    return render(request, 'core/ais.html', {
        'active': 'ais',
            })
