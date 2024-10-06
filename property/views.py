from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView , DetailView
from .models import Property

class PropertyList(ListView):
    model = Property
    paginate_by = 1
    # filter


class PropertyDetails(DetailView):
    model = Property
    ## Book

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
