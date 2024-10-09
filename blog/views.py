from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 2

class PostDetail(DetailView):
    model = Post



