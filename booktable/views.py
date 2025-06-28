from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking, UserProfile


# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = "booktable/index.html"


class BookingListView(generic.ListView):
    #model = Booking
    queryset = Booking.objects.all()
    template_name = "booktable/booktable_list.html"

    

'''
def booking(request):
    return HttpResponse("Hello, Welcome user!, this is the booking page.")


def homePage(request):
    return render(request, 'index.html')


def aboutPage(request):
    return HttpResponse("This is about page")


def loginPage(request):
    return render(request, 'login.html')


def signupPage(request):
    return render(request, 'signup.html')


def menuPage(request):
    return HttpResponse("View this menu")
'''