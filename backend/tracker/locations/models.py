from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from locations.validations import name_validator, mail_validator, pass_validator, coordinates_validator

#the model which contains all the user details that we need
class Profile(User):
    user = User.username
    password = User.password
    first_name = User.first_name
    last_name = User.last_name
    email = User.email

#the Locations model which contains a fk to the user model   
class Locations(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    latitude = models.FloatField(validators=[coordinates_validator])
    longitude = models.FloatField(validators=[coordinates_validator])
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    