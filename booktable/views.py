from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking, UserProfile
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookTableForm


# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = "booktable/index.html"


class MenuView(TemplateView):
    template_name = 'booktable/menu.html'


class AboutPageView(TemplateView):
    template_name = 'booktable/aboutus.html'

#This is a class based view that lists all bookings in the database.
class BookingListView(LoginRequiredMixin, generic.ListView):

    template_name = "booktable/booktable_list.html"
    context_object_name = 'bookings'
    paginate_by = 5

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_count'] = Booking.objects.filter(user=self.request.user).count()
        return context
    

class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = UserProfile
    template_name = "booktable/user_profile.html"
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    #fields = ['table_size', 'booking_date', 'booking_time', 'allergies']
    form_class = BookTableForm
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
        form.instance.user = self.request.user  
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user
    

def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user) 

    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')

    return render(request, 'booktable/confirm_delete.html', {'booking': booking})


class PrivacyPolicyView(TemplateView):
    template_name = "booktable/privacy_policy.html"
