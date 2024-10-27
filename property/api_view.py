from .models import Property
from .serializers import PropertySerializers
from rest_framework.generics import ListAPIView


class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
