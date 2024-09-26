from django.urls import path
from .views import PropertyList , PropertyDetails

app_name = 'peroperty'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>',PropertyDetails.as_view() , name = 'property_detail')
]
