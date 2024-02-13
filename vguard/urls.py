"""
URL configuration for vguard project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Endpoint for managing users resources
    path('', include('core.urls')),  # Customized drf-passwordless-auth urls 
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint for requesting an access token using the refresh token
]
