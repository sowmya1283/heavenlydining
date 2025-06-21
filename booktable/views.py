from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking(request):
    return HttpResponse("Hello, Welcome user!, this is the booking page.")