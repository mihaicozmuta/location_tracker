from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from locations.validations import name_validator, mail_validator, pass_validator

#the model which contains all the user details that we need
class Profile(User):
    user = User.username
    password = User.password
    first_name = User.first_name
    last_name = User.last_name
    email = User.email

   
class Locations(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    