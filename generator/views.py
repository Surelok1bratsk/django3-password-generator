from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters =  list(string.ascii_lowercase)   # все символы анлийского языка в нижнем регистре

    if request.GET.get('uppercase'):    # если есть буквы в верхнем регистре
        characters.extend([x.upper() for x in characters])  # то переводим все значения в списке characters в верхний регистр
    if request.GET.get('special'):    # если есть специальные символы
        characters.extend(string.punctuation) # добавляем в список специальные символы
    if request.GET.get('numbers'):    # если есть цифры
        characters.extend([str(x) for x in range(10)]) # добавляем в список цифры от 0 до 9

    length = int(request.GET.get('length', 12)) # длина пароля (12 по умолчанию)
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})