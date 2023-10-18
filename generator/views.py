import re

from django.http import HttpResponse
from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list("qwertyuiopasdfghjklzxcvbnm")
    length = int(request.GET.get('length'))
    if request.GET.get('nums'):
        characters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-=.,'))
    the_password = ''
    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
