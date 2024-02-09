from django.urls import path, include
from drfpasswordless.urls import urlpatterns as drfpasswordless_urls
from core.views import CustomObtainAuthTokenFromCallbackToken
from drfpasswordless.settings import api_settings

# Exclude unwanted endpoints from the drfpasswordless URLs
excluded_endpoints = [
    'auth_mobile',  # Exclude the auth_mobile endpoint
    'verify_mobile',  # Exclude the verify_mobile endpoint
    'auth_token',  # Exclude the auth_token endpoint
]

# Filter out excluded endpoints from the drfpasswordless URLs
filtered_urls = [url for url in drfpasswordless_urls if url.name not in excluded_endpoints]


urlpatterns = [
    # Include filtered drfpasswordless URL patterns
    path('', include(filtered_urls)),
    path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'token/', CustomObtainAuthTokenFromCallbackToken.as_view(), name='auth_token'),
]

