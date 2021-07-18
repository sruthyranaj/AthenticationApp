from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('accounts/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]