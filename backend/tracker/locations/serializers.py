from rest_framework import serializers, permissions
from locations.models import Profile, Locations
from django.contrib.auth.models import User


#Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username','first_name', 'last_name')
        

#serializer for the user registration 
class UserRegistration(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name', 'last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

#we override the create method
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Profile(**validated_data)
        user.set_password(password)
        user.save()
        return user


#serializer for locations (Locations)
class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'
        

    
        

