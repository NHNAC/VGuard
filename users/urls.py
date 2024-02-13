from django.urls import path
from .views import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

