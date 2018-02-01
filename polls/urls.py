# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:27:56 2018

@author: ewharton
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
]    