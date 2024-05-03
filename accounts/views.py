from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = 'home'  # Redirect to this URL after successful login

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return super().form_invalid(form)
def logout_view(request):
    logout(request)
    return redirect('login')