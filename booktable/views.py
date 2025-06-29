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
    queryset = Booking.objects.all().order_by('-booking_date')
    template_name = "booktable/booktable_list.html"
    context_object_name = 'bookings'
    paginate_by = 5


class UserProfileView(generic.DetailView):
   # model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = "booktable/user_profile.html"
    context_object_name = 'user_profile'

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