from django.conf.urls import include , url
from . import views

urlpatterns = [
    url(r'^$',views.top, name='top'),
    url(r'^result',views.result, name='result'),
    url(r'^town/$', views.town_list,name="town_list"),
    url(r'^town/info/$',views.city_info,name='city_info'),
]