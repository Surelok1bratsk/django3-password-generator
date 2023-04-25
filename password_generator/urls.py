"""
URL configuration for password_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from generator import views

''' password/ (первый параметр) - может быть луюбое имя, если установлена связь через переменную 'name' 
                                  с формой (например 'home.html'), которая прописывается в форме 
                                  (form action="{% url 'password' %}"). 
                                  Также значение может оканчиваться на '/' или без '/'. это влияет только на 
                                  то, как будет отображаться адрес страницы - с '/' или без. '''
urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]
