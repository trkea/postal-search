#coding: utf-8
from django.shortcuts import render
import requests
import json
import ast
from .models import Place
from .forms import PlaceForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


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
    if request.GET.get('datatype') == None:
        return render(request, 'top.html')
    model = Place(
        city='a',
        town='a',
        prefecture='a',
        postal='12345',
        x=12,
        y=15
    )
    model.prefecture = 'b'
    model.city = 's'
    model.town = 'f'
    model.postal = 'g'
    model.x = 120
    model.y = 12
    model.save
    return render(request, 'top.html')


def result(request):
    keyword = request.GET.get('place')
    result = search(keyword)
    results = sorted(result, key=lambda x: x['prefecture'])
    return render(request, 'search-result.html',{'result': results})


def town_list(request):
    town = request.GET.get('select')
    town_list = search(town)
    sort_townName_list = sorted(town_list, key=lambda x: x['city_kana'])
    sort_cityName_list = sorted(sort_townName_list, key=lambda x: x['town_kana'])
    return render(request, 'town_list.html', {'town_list': sort_cityName_list,'town_name': town})


def city_info(request):
    selected = request.GET.get('selected')
    city = ast.literal_eval(selected)
    postal = city['postal']
    city['postal'] = '{0}{1}{2}'.format(postal[:3], '-', postal[3:])
    return render(request, 'city_info.html', {'city': city})


def favorite(request):
    model = get_object_or_404(Place)
    model.prefecture = request.GET.get('prefecture')
    model.city = request.GET.get('city')
    model.town = request.GET.get('town')
    model.postal = request.GET.get('postal')
    model.x = request.GET.get('x')
    model.y = request.GET.get('y')
    model.save()
    response = render(request, 'city_info.html')
    return HttpResponse(response)