from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import RegisterVerificationRequestModel

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=False, widget= forms.HiddenInput())

    first_name = forms.CharField(max_length=30, required=False, widget= forms.HiddenInput())

    last_name = forms.CharField(max_length=30, required=False, widget= forms.HiddenInput())

    email = forms.EmailField(required=False, widget= forms.HiddenInput())

    password1 = forms.CharField(widget=forms.PasswordInput)

    password2 = forms.CharField(widget= forms.PasswordInput)

    verification_code = forms.CharField(widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'username', 'verification_code']



class RegistrationRequestForm(forms.ModelForm):
    class Meta:
        model = RegisterVerificationRequestModel
        fields = ['first_name', 'last_name', 'email']



        