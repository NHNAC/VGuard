from rest_framework import permissions
from django.conf import settings


class HasKey(permissions.BasePermission):
    """
    Custom permission class that checks for a valid API key in the request header.
    """
    def has_permission(self, request, view):
        # Get the API key from the request headers
        api_key = request.headers.get('Api-Key')

        # Check if the API key matches the one from settings
        return bool(api_key and api_key == settings.API_KEY)