from rest_framework import serializers
from locations.models import Client

#serializer
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
