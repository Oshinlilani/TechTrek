from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")

def headphone(request):
    return render(request, "headphone.html")

def loginPage(request):
    return render(request, "loginPage.html")

def smartwatch(request):
    return render(request, "smartwatch.html")

def register(request):
    return render(request, "registerPage.html")

def order(request):
    return render(request, "order.html")

def earbud(request):
    return render(request, "earbud.html")
