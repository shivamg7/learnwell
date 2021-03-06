from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.test import SimpleTestCase, override_settings
from django.conf.urls.static import static

from . import views


app_name = 'bsl'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/', views.showQuiz, name='quiz'),
    path('submitAnswer/<int:questionId>/<str:answer>', views.submitAnswer, name='submitAnswer'),
    path('stats/', views.stats, name='stats'),
    path('results/', views.results, name='results'),    
]
