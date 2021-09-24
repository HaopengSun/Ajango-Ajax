from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm
