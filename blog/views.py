from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
from taggit.models import Tag
# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 2

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['tags'] =  Tag.objects.all()
        return context
    



