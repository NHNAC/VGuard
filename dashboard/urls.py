from rest_framework import routers
from .views import CameraViewSet, FireSmokeWeaponDetectionViewSet, AgeGenderViewSet, FaceRecognitionViewSet, LicensePlateRecognitionViewSet

router = routers.DefaultRouter()
router.register('camera', CameraViewSet)
router.register('detection', FireSmokeWeaponDetectionViewSet)
router.register('agegender', AgeGenderViewSet)
router.register('facerecog', FaceRecognitionViewSet)
router.register('platerecog', LicensePlateRecognitionViewSet)
urlpatterns = router.urls
