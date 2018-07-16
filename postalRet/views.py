from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from collections import OrderedDict
import ast
#coding: utf-8

def search(keyword):
    url = 'http://geoapi.heartrails.com/api/json?method=suggest&matching=like&keyword=' + keyword
    html = requests.get(url).text
    result = json.loads(html)
    if not 'location' in result['response']:
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
    return render(request, 'search-result.html',{'result':results})

def town_list(request):
    town = request.GET.get('select')
    town_list = search(town)
    return render(request, 'town_list.html',{'town_list':town_list,'town_name':town})

def city_info(request):
    selected = request.GET.get('selected')
    city = ast.literal_eval(selected)
    return render(request,'city_info.html',{'city':city})    

