from .models import Property
from .serializers import PropertySerializers
from rest_framework.generics import ListAPIView , RetrieveAPIView


class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

class PropertyAPIDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

