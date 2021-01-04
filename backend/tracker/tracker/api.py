from rest_framework import routers
from locations.api_views import UserViewset, LocationsViewset, RegistrationView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
#we register the viewsets used in .api_views
router.register(r'users', UserViewset)
router.register(r'locations', LocationsViewset)
router.register(r'register', RegistrationView, basename='register')
