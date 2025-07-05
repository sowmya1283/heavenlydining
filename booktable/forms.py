from allauth.account.forms import SignupForm
from django import forms
from booktable.models import UserProfile, Booking
from django.utils import timezone


class CustomSignupForm(SignupForm):
    phone_number = forms.IntegerField(
        label='Phone Number', 
        required=False, 
        help_text='Optional. Please enter your phone number.')
    address = forms.CharField(
        label='Address', 
        required=False, 
        help_text='Optional. Please enter your address.')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        UserProfile.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address']
        )

        return user
    

class BookTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table_size', 'booking_date', 'booking_time', 'allergies']

    def clean_booking_date(self):
        date = self.cleaned_data.get('booking_date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return date
    
    def clean_booking_time(self):
        time = self.cleaned_data.get('booking_time')
        if time and (time.hour < 10 or time.hour > 22):
            raise forms.ValidationError("Booking time must be between 10:00 & 22:00.")
        return time
    
    def clean_table_size(self):
        size = self.cleaned_data.get('table_size')
        if size is None:
            raise forms.ValidationError("Table size is required.")
        if size and (size < 1 or size > 20):
            raise forms.ValidationError("Table size must be a positive integer between 1 and 20.")
        return size
