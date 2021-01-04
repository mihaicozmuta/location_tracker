from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from rest_framework import permissions
import django_filters

#if check wheter the user making the request is a super-user
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


#this class checks if the request.user is the "owner" of the Profile
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.id == request.user.id
        else:
            return False

class IsLocationOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return request.user.id == obj.id
            return False

class LocationFiltering(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.user.id == request['user']
        else:
            return False
