from locations.models import Client
from rest_framework import viewsets, permissions
from .serializers import user_serializer



#Clients' viewset
class user_viewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permissions_classes =  [
        permissions.AllowAny()
    ]
    serializer_class = user_serializer