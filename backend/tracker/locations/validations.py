from rest_framework import serializers



def name_validator(name:str):
    if name is None:
        raise serializers.ValidationError("The name cannot be empty")
    return name

def mail_validator(mail:str):
    if '@' not in mail:
        raise serializers.ValidationError('This is not a vaild e-mail')
    return mail 


def pass_validator(pwd:str):
    if pwd is None:
        raise serializers.ValidationError('Please include a password')
    elif len(pwd) < 7:
        raise serializers.ValidationError('The password must have least 8 characters')
    return pwd


def coordinates_validator(lat:float):
    if lat is None:
        raise serializers.ValidationError('Please include both latitude and longitude')
    if lat < 0:
        raise serializers.ValidationError('Latitude and Longitude cannot be negative numbers')