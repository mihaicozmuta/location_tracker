from rest_framework import serializers, permissions
from locations.models import Profile, Locations

#serializer for user information (Profile)
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        permissions_classes = [
            permissions.AllowAny
        ]
        fields = '__all__'

#serializer for locations (Locations)

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'

