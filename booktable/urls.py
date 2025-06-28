from django.shortcuts import render
from django.views import generic
from .models import Booking, UserProfile
from django.urls import path, include
from . import views
from .views import HomePageView, BookingListView


#This pattern tells Django to look in the booktable app URL file for any bookingtable urlpatterns.
urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("booking", views.BookingListView.as_view(), name="booking_list"),

]
