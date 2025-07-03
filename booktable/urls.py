from django.shortcuts import render
from django.views import generic
from .models import Booking, UserProfile
from django.urls import path, include
from . import views
from .views import HomePageView, BookingListView, BookingCreateView, BookingUpdateView, UserProfileView, delete_booking


#This pattern tells Django to look in the booktable app URL file for any bookingtable urlpatterns.
urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("booking/", views.BookingListView.as_view(), name="booking_list"),
    path("userprofile/<str:username>/", views.UserProfileView.as_view(), name="user_profile"),
    path('book/', BookingCreateView.as_view(), name="book_table"),
    path('booking/<int:pk>/edit/', BookingUpdateView.as_view(), name="edit_booking"),
    path('booking/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
]
