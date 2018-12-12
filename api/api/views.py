# coding: utf-8
from django.shortcuts import render


def home(request):
    context = {'foo': 'bar'}
    return render(request, 'home.html', context)
