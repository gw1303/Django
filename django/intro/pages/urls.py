from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index),
    path('hello/<name>/', views.hello),

    # 두 수를 입력 받아 곱한 결과를 보여주는 페이지
    path('mul/<fir>/<sec>/', views.mul),

    path('dtl/', views.dtl),

    # 생일인지 아닌지 알려주는 페이지
    path('isityourbirthday/', views.isityourbirthday),

    # 값을 주고받는 페이지
    path('throw/', views.throw),
    path('catch/', views.catch),

    # 로또번호 생성기 
    path('lotto/', views.lotto),
    path('generate/', views.generate),

    # 새로운 유저 함수 생성 (POST 방식)
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),


]


