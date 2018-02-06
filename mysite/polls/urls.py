# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:27:56 2018

@author: ewharton
"""

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
]
        
        
   