from rest_framework import viewsets
from api.serializers import CameraSerializer
from devices.models import Camera


# REST API
class CameraView(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

