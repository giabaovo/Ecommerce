from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def login(request):
    context = {}
    return render(request, 'store/login.html', context)


def register(request):
    context = {}
    return render(request, 'store/register.html', context)
