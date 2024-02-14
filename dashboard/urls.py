from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('camera', views.CameraViewSet)
urlpatterns = router.urls
