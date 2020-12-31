from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login', obtain_auth_token, name='api_token_auth'), 
]
