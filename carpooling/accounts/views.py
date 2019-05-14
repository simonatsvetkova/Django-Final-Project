from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.


class UserDetails(generic.DeleteView):
    model = 

class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = ''
    template_name = ''

