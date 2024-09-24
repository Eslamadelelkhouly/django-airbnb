from django.contrib import admin

# Register your models here.

from .models import Property , PropertyBook , PropertyImages , PropertyReview , Category

admin.site.register(Property)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
