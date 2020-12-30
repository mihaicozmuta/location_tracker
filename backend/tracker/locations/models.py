from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from locations.validations import name_validator, mail_validator, pass_validator

#the model which contains all the user details that we need
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, validators=[name_validator])
    last_name = models.CharField(max_length=100, validators=[name_validator])
    email = models.CharField(max_length=100, validators=[mail_validator])
    created_at = models.DateTimeField(auto_now_add=True)

class Locations(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    latitute = models.FloatField()
    longitude = models.FloatField()
    