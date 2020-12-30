from rest_framework import routers
from locations.api_views import UserViewset, LocationsViewset

router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'locations', LocationsViewset)
