#coding: utf-8
from django.shortcuts import render
import requests
import json
import ast
from django.shortcuts import render


def search(keyword):
    prefecture_list = \
        ['北海道', '青森', '岩手', '宮城', '秋田',
         '山形', '福島', '茨城', '栃木', '群馬',
         '埼玉', '千葉', '神奈川', '新潟', '富山',
         '石川', '福井', '山梨', '長野', '岐阜',
         '静岡', '愛知', '三重', '滋賀', '兵庫',
         '奈良', '和歌山', '鳥取', '島根', '岡山',
         '広島', '山口', '徳島', '香川', '愛媛',
         '高知', '福岡', '佐賀', '長崎', '熊本',
         '大分', '宮崎', '鹿児島', '沖縄']
    if keyword in prefecture_list:
        keyword += '県'
    elif keyword in ['京都', '大阪']:
        keyword += '府'
    url = 'http://geoapi.heartrails.com/api/json?method=suggest&matching=like&keyword=' + keyword
    if keyword == '東京' or keyword == '東京都':
        url = 'http://geoapi.heartrails.com/api/json?method=suggest&matching=prefix&keyword=' + keyword
    html = requests.get(url).text
    result = json.loads(html)
    if not 'location' in result['response']:
        list = []
        result['prefecture'] = '見つかりませんでした'
        result['city'] = None
        list.append(result)
        return list
    return result['response']['location']


def top(request):
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