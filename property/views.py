from django.shortcuts import render , redirect
from django.views.generic.edit import FormMixin

# Create your views here.

from django.views.generic import ListView , DetailView
from .models import Property
from .forms import PropertyBookForm
from .filters import PropertyFilter

class PropertyList(ListView):
    model = Property
    paginate_by = 1
    # filter


class PropertyDetails(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm
    ## Book

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context

    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            
            return redirect('/')
