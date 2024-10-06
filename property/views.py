from django.shortcuts import render
from django.views.generic.edit import FormMixin

# Create your views here.

from django.views.generic import ListView , DetailView
from .models import Property

class PropertyList(ListView):
    model = Property
    paginate_by = 1
    # filter


class PropertyDetails(FormMixin,DetailView):
    model = Property
    ## Book

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context

    def post(self,request,*args, **kwargs):
        

