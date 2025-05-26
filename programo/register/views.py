from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import UserRegisterForm, RegistrationRequestForm
from .models import RegisterVerificationRequestModel
import random
import string


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationRequestForm(request.POST)
        if form.is_valid():
            registration_request = form.save()
            verification_code = registration_request.verification_code
            request.session['verification_code'] = verification_code
            request.session['user_data'] = {
                'first_name' : form.cleaned_data.get('first_name'),
                'last_name' : form.cleaned_data.get('last_name'),
                'email' : form.cleaned_data.get('email'),
                'phone' : form.cleaned_data.get('phone'),
                'password1' : form.cleaned_data.get('password1'),
                'password2' : form.cleaned_data.get('password2'),
            }

            send_mail(
                'Your verification code',
                f'Your verification code is {verification_code}',
                'noreplay@yourdomain.com',
                [form.cleaned_data.get('email')],
            )

            messages.info(request, 'A verification code has been send to your email')
            return redirect('verify', pk = registration_request.id)
    else:
        form = RegistrationRequestForm()
    return render(request, 'users/register.html', {'form' : form})




def verify(request, pk):
    if request.method == 'POST':
        data = request.POST
        data = {}
        data['password1'] = request.POST.get('password1')
        data['password2'] = request.POST.get('password2')
        data['verification_code'] = request.POST.get('verification_code')

        registration_request = get_object_or_404(RegisterVerificationRequestModel, pk=pk)

        validation_code_from_data_base = registration_request.verification_code
        data['username'] = registration_request.first_name[0] + registration_request.last_name + str(random.randint(1, 9999))
        data['first_name'] = registration_request.first_name
        data['last_name'] = registration_request.last_name
        data['email'] = registration_request.email
        user_registration_form = UserRegisterForm(data)
        if user_registration_form.is_valid():

            print(user_registration_form.cleaned_data)
            validation_code_from_user = user_registration_form.cleaned_data.get('verification_code')
            if validation_code_from_user == validation_code_from_data_base:
                user_registration_form.save()
                messages.success(request, f'Contul tau a fost creat cu succes! Numele tau de utilizator este: {data['username']}')

                return redirect('home-page')
            
            else:
                return HttpResponse(401)
        return render(request, 'accounts/verify.html')


    else:
        user_registration_form = UserRegisterForm()
    return render(request, 'accounts/verify.html', {'form': user_registration_form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():

            user = form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                return redirect('client-page')
            
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form' : form})



