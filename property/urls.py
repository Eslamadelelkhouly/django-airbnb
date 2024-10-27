from django.urls import path
from .views import PropertyList , PropertyDetails
from .api_view import PropertyAPIList

app_name = 'peroperty'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>',PropertyDetails.as_view() , name = 'property_detail'),
    path('api/list',PropertyAPIList.as_view(), name='property_list_api'),

]
