from rest_framework import serializers
from .models import Camera, FireSmokeWeaponDetection


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'name', 'notes', 'location', 'latitude', 'longitude']
