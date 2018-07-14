from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from collections import OrderedDict
#coding: utf-8

def search(keyword):
    url = 'http://geoapi.heartrails.com/api/json?method=suggest&matching=like&keyword=' + keyword
    html = requests.get(url).text
    result = json.loads(html)
    if not 'location' in result:
        list = []
        result = {}
        result['prefecture'] = '見つかりませんでした'
        result['city'] = None
        list.append(result)
        return list
    return result['response']['location']

# Create your views here.
def top(request):
	return render(request, "top.html")

def result(request):
    keyword = request.GET.get('place')
    result = search(keyword)
    results =  sorted(result,key=lambda x:x['prefecture'])
    return render(request, 'searchResult.html',{'result':results})



