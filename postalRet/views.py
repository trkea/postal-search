#coding: utf-8
from django.shortcuts import render
import requests
import json
import ast

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


def top(request):
	return render(request, "top.html")

def result(request):
    keyword = request.GET.get('place')
    result = search(keyword)
    results = sorted(result,key=lambda x:x['prefecture'])
    return render(request, 'search-result.html',{'result':results})

def town_list(request):
    town = request.GET.get('select')
    town_list = search(town)
    sort_townName_list = sorted(town_list, key=lambda x: x['city_kana'])
    sort_cityName_list = sorted(sort_townName_list, key=lambda x: x['town_kana'])
    return render(request, 'town_list.html',{'town_list':sort_cityName_list,'town_name':town})

def city_info(request):
    selected = request.GET.get('selected')
    city = ast.literal_eval(selected)
    postal = city['postal']
    city['postal'] = '{0}{1}{2}'.format(postal[:3],'-',postal[3:])
    return render(request,'city_info.html',{'city':city})    

