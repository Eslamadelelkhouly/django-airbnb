from django.shortcuts import render
from django.views.generic import ListView
from .models import About , FAQ
# Create your views here.

class AboutView(ListView):
    model = FAQ