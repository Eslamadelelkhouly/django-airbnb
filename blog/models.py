from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="post_author", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post/')
    created_At = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', verbose_name="post_category", on_delete=models.CASCADE, related_name="post_category")
    slug = models.SlugField(null=True , blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    
    def __str__(self):
            return self.title


    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
            return self.name
    