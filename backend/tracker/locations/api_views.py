from locations.models import Profile, Locations
from . import models
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, LocationsSerializer, UserRegistration
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from locations.permissions import IsSuperUser, IsOwner

class UserAuthentication(ObtainAuthToken):
    def post(self, requests, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_Create(user=user)
        return Response(token.key)


#Users' viewset
class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'delete', 'put', 'patch']
    def get_permissions(self):
        # Overrides to tightest security: Only superuser can create, update, partial update, destroy, list
        self.permission_classes = [IsSuperUser]

        # Allow only by explicit exception
        if self.action == 'retrieve':
            self.permission_classes = [IsOwner]

        return super(self.__class__, self).get_permissions()
    #permission_classes = [permissions.AllowAny]

#Locations viewset
class LocationsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Locations.objects.all()
    serializer_class = LocationsSerializer

#Registration view
class RegistrationView(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = UserRegistration

