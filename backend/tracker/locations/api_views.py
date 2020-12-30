from locations.models import Profile, Locations
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer, LocationsSerializer
from rest_framework.permissions import IsAuthenticated 


#Clients' viewset
class UserViewset(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#Locations viewset
class LocationsViewset(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer