from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Camera, FireSmokeWeaponDetection, AgeGender, FaceRecognition, LicensePlateRecognition
from .serializers import CameraSerializer, FireSmokeWeaponDetectionSerializer, AgeGenderSerializer, FaceRecognitionSerializer, LicensePlateRecognitionSerializer
from .permissions import HasKey

class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [IsAuthenticated | HasKey]

class FireSmokeWeaponDetectionViewSet(viewsets.ModelViewSet):
    queryset = FireSmokeWeaponDetection.objects.all()
    serializer_class = FireSmokeWeaponDetectionSerializer


class AgeGenderViewSet(viewsets.ModelViewSet):
    queryset = AgeGender.objects.all()
    serializer_class = AgeGenderSerializer


class FaceRecognitionViewSet(viewsets.ModelViewSet):
    queryset = FaceRecognition.objects.all()
    serializer_class = FaceRecognitionSerializer


class LicensePlateRecognitionViewSet(viewsets.ModelViewSet):
    queryset = LicensePlateRecognition.objects.all()
    serializer_class = LicensePlateRecognitionSerializer
    
