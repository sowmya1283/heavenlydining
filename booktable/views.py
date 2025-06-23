from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def booking(request):
    return HttpResponse("Hello, Welcome user!, this is the booking page.")


def homePage(request):
    return render(request, 'index.html')


def aboutPage(request):
    return HttpResponse("This is about page")


def contactPage(request):
    return HttpResponse("This is contact page")


def menuPage(request):
    return HttpResponse("View this menu")
