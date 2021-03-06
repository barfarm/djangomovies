from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SubmittableAuthenticationForm, SubmittablePasswordChangeForm, SignUpForm


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class=SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url=reverse_lazy('index')

class SuccessMessagedLogoutView(LogoutView):
    def get_next_page(self):
        result=super().get_next_page()
        messages.success(self.request,'Succesfully logetout')

class SignUpView (CreateView):
    template_name='form.html'
    form_class=SignUpForm
    success_url=reverse_lazy('index')