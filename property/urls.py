from django.urls import path
from .views import PropertyList , PropertyDetails

app_name = 'peroperty'

urlpatterns = [
    path('',PropertyList.as_view()),
    # path('',PropertyDetails.as_view())
]
