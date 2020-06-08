# Django

## 가상환경 만들기

> 디렉토리 생성

```bash
$ mkdir 디렉토리명
$ cd 디렉토리명
```

> 가상환경 생성

```bash
$ python -m venv 가상환경명
```

> 가상환경 사용

```bash
C:\Users\Name\디렉토리명> 가상환경명\Scripts\activate
```



> Django 설치

```bash
(myvenv) ~$ python -m pip install --upgrade pip

(myvenv) ~$ pip install django==2.2.13
```



## Django 활용

> Django project 만들기

```bash
django-admin 
```





> 서버 실행

```bash
(myvenv) ~$ python manage.py runserver
```



> app 만들기

```bash
(myvenv) ~$ python manage.py startapp app이름 
```



### MVC 패턴

> Model, View, Controller의 3가지 형태로 웹을 구성함



> urls.py에 사용할 views 연결

```bash
# urls.py

from django.contrib import admin
from django.urls import path

# pages app의 views.py import
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', )views.index,
]
```



> s

```bash
(myvenv) ~$ 
```



> s

```bash
(myvenv) ~$ 
```



> s

```bash
(myvenv) ~$ 
```



> s

```bash
(myvenv) ~$ 
```



