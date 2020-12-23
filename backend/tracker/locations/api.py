from locations.models import Client
from rest_framework import viewsets, permissions
from .serializers import user_serializer
from rest_framework.permissions import IsAuthenticated 



#Clients' viewset
class user_viewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated) 
    queryset = Client.objects.all()
    permissions_classes =  [
        permissions.AllowAny()
    ]
    serializer_class = user_serializer