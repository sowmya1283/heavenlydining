from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking, UserProfile
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Booking


# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = "booktable/index.html"

#This is a class based view that lists all bookings in the database.
class BookingListView(generic.ListView):
    queryset = Booking.objects.all().order_by('-booking_date')
    template_name = "booktable/booktable_list.html"
    context_object_name = 'bookings'
    paginate_by = 5
    booking_count = Booking.objects.count()
    
    '''
    return render(
        request,
        "booktable/booktable_list.html",
        {
            "User": Booking.user,
            "Booking Date": Booking.booking_date,
            "Booking Time": Booking.booking_time,

        }

    )
    '''



class UserProfileView(LoginRequiredMixin,generic.DetailView):
    model = UserProfile
    template_name = "booktable/user_profile.html"
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['table_size', 'booking_date', 'booking_time', 'allergies']
    template_name = 'booktable/book_table.html'
    success_url = reverse_lazy('booking_list') # or redirect to a confirmation page

    def form_valid(self, form):
        """
        Override form_valid to associate the booking with the logged-in user.
        """
        form.instance.user = self.request.user # Associate the booking with the logged-in user
        return super().form_valid(form)
    
class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    fields = ['table_size', 'booking_date', 'booking_time', 'allergies']
    template_name = 'booktable/edit_booking.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self,form):
        form.instance.user = self.request.user  # Associate the booking with the logged-in user
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user