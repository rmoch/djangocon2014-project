# -*- coding: utf-8 -*-

import json
import requests
import xmltodict

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'core/index.html', {
        'active': 'index',
            })


def aisproxy(request):
    bbox = request.GET['bbox']
    response = requests.get('http://map.openseamap.org/api/getAIS.php?bbox=' + bbox)
    data = xmltodict.parse(response.content)
    print data
    return HttpResponse(json.dumps(data), content_type='application/json; charset=utf-8')
