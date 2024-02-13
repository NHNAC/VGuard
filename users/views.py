from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

# viewset for managing users
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
