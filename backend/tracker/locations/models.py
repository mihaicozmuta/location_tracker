from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from locations.validations import name_validator, mail_validator

#the model which contains all the user details that we need
class Client(models.Model):
    first_name = models.CharField(max_length=100, validators=[name_validator])
    last_name = models.CharField(max_length=100, validators=[name_validator])
    email = models.CharField(max_length=100, unique=True, validators=[mail_validator])
    password = User.password
    created_at = models.DateTimeField(auto_now_add=True)
