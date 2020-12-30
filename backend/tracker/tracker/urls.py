from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
