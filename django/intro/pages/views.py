from django.shortcuts import render
import numpy as np

# Create your views here.

def index(request) :
    
    hello = 'hello ~ ~ '
    lunch = '라멘'
    
    context = {
        'hello':hello,
         'l':lunch,
    }

    return render(request, 'pages/index.html', context)


def hello(request, name) :

    context = {
        'name':name
    }

    return render(request, 'pages/hello.html', context)


def mul(request, fir, sec) :

    context = {
        'fir' : fir,
        'sec' : sec,
        'res' : (int(fir) * int(sec))
    }

    return render(request, 'pages/mul.html', context)

from datetime import datetime

def dtl(request) :

    foods = ['짜장면','탕수육','짬뽕','양장피']
    sentence = 'Life is short, you need python'
    fruits = ['apple','banana','cucumber','mango']
    datetimenow = datetime.now
    empty_list = []

    context = {
        'foods' : foods,
        'sentence':sentence,
        'fruits':fruits,
        'datetimenow':datetimenow,
        'empty_list':empty_list,
    }
    
    return render(request, 'pages/dtl.html', context)

def isityourbirthday(request) :
    # 1. 오늘 날짜 가져오기
    today = datetime.now()
    # 2. month, day 가져와서 비교하기
    month = today.month
    day = today.day

    context = {
        'month':month,
        'day':day
    }

    return render(request, 'pages/isityourbirthday.html', context)


def throw(request) :

    context = {
        
    }

    return render(request, 'pages/throw.html', context)

def catch(request) :

    message = request.GET.get('message')
    username = request.GET.get('username')
    context = {
        'message':message,
        'username':username
    }

    return render(request, 'pages/catch.html', context)

def lotto(request) :
    context = {

    }

    return render(request, 'pages/lotto.html', context)



def generate(request) :

    n = int(request.GET.get('n'))

    res = []
    while len(res) != n :
        res.append(np.random.randint(1,46))
        res = list(set(res))
    res.sort()

    context = {
        'res' : res
    }

    return render(request, 'pages/generate.html', context)

def user_new(request) :

    context = {

    }

    return render(request, 'pages/user_new.html',context)

def user_create(request) :

    username = request.POST.get('username')
    pw = request.POST.get('pw')

    context = {
        'username':username,
        'pw':pw
    }

    return render(request, 'pages/user_create.html', context)



