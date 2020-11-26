from rest_framework import serializers




def latitude_restriction(lat):
    if lat > 20:
        raise serializers.ValidationError("the latitude should be smaller than 20")
    return lat


def name_validator(name:str):
    if name is None:
        raise serializers.ValidationError("The name cannot be empty")
    return name