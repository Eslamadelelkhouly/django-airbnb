from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey("Place", on_delete=models.CASCADE, verbose_name="property_place", related_name='properties')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="property_category", related_name='properties')
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True , blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property,self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.name


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="property_image", related_name='property_image')
    image = models.ImageField(upload_to='propertyimages/')
    
    def __str__(self):
        return str(self.property)


class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class PropertyReview(models.Model):  # Fixed typo here
    author = models.ForeignKey(User, verbose_name="review_author", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, verbose_name="review_property", on_delete=models.CASCADE)  # Fixed typo here
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.property)  # Fixed typo here

COUNT = (
    (1,1),
    (2,1),
    (3,1),
    (4,1),
)

class PropertyBook(models.Model):  # Fixed typo here
    user = models.ForeignKey(User, verbose_name="book_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, verbose_name="book_property", on_delete=models.CASCADE)  # Fixed typo here
    date_from = models.DateField(default = timezone.now)
    date_to = models.DateField(default = timezone.now)
    guest = models.CharField(max_length= 2 , choices=COUNT)
    children = models.CharField(max_length= 2 , choices=COUNT)

    def __str__(self):
        return str(self.property)