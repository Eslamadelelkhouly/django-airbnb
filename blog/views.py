from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q
# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 2

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count = Count('post_category'))
        context['tags'] =  Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    

class PostByCategory(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains = slug)
        )
    



class PostByTags(ListView):
    model = Post


