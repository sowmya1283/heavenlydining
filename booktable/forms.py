from allauth.account.forms import SignupForm
from django import forms
from booktable.models import UserProfile


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