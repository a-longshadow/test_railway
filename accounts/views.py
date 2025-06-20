from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('blog:home')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('blog:home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}! You can now log in.')
        login(self.request, self.object)
        return response


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have been logged out successfully.')
        return super().dispatch(request, *args, **kwargs)
