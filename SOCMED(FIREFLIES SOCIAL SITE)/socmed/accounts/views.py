from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # Reverse lazy redirects user to the login page when it ticks the button
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
