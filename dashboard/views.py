from rest_framework import viewsets
from .models import Camera
from .serializers import CameraSerializer
# Create your views here.

class CameraViewSet(viewsets.ModelViewSet):
  queryset = Camera.objects.all()
  serializer_class = CameraSerializer
