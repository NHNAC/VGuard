"""
URL configuration for vguard project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Endpoint for managing users resources
    # path('', include('core.urls')),  # Customized drf-passwordless-auth urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint for requesting an access token and refresh token 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint for requesting an access token using the refresh token
    path('dashboard/', include('dashboard.urls'))  # Endpoint for managing dashboard resources,  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
