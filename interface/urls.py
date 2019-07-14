# -*- coding : utf-8 -*-
# @author : Dell
# @time : 16:53   2019/7/14
# @filename : urls.py
from django.urls import path
from .views import index
urlpatterns=[
    path('qrcode/',index,name='二维码'),
]