from rest_framework import viewsets
from .models import Camera, FireSmokeWeaponDetection, AgeGender, FaceRecognition, LicensePlateRecognition
from .serializers import CameraSerializer, FireSmokeWeaponDetectionSerializer, AgeGenderSerializer, FaceRecognitionSerializer, LicensePlateRecognitionSerializer


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


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
    
