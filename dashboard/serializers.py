from rest_framework import serializers
from .models import Camera, FireSmokeWeaponDetection, AgeGender, FaceRecognition, LicensePlateRecognition


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'name', 'notes', 'location', 'latitude', 'longitude']


class FireSmokeWeaponDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireSmokeWeaponDetection
        fields = ["camera", "alarm_title", "severity", "status"]


class AgeGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGender
        fields = ["camera", "male_kids", "female_kids", "male_teens", "female_teens", "male_adults", "female_adults", "male_old", "female_old"]


class FaceRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = ["camera", "image"]


class LicensePlateRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensePlateRecognition
        fields = ["camera", "plate_number"]

