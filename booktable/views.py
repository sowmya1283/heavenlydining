from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def booking(request):
    return HttpResponse("Hello, Welcome user!, this is the booking page.")


def homePage(request):
    return HttpResponse("This is home page")


def aboutPage(request):
    return HttpResponse("This is about page")


def contactPage(request):
    return HttpResponse("This is contact page")


def menuPage(request):
    return HttpResponse("View this menu")
