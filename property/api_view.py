from .models import Property
from .serializers import PropertySerializers
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.permissions import IsAuthenticated



class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
    permission_classes = [IsAuthenticated]


class PropertyAPIDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
    permission_classes = [IsAuthenticated]


