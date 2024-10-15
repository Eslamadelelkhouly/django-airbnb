from django.shortcuts import render
from property .models import Property , Place
from django.db.models.query_utils import Q
# Create your views here.


def home(request):
    places = Place.objects.all()
    return render(request , 'settings/home.html',{'places':places},)


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    property_list = Property.objects.filter(
        Q(name__icontains = name)&
        Q(place__name__icontains = place)
    )
    return render(request ,'settings/home_search.html',{'property_list':property_list})
