from django.shortcuts import render
from property .models import Property , Place
# Create your views here.


def home(request):
    places = Place.objects.all()
    return render(request , 'settings/home.html',{'places':places},)