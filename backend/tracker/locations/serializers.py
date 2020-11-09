from rest_framework import serializers
from locations.models import Client

#serializer
class user_serializer(serializers.ModelSerializer):

    class Metta:
        model = Client
        fiels = '__all__'
