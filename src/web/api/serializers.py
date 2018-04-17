from rest_framework import serializers
from devices.models import Camera


# Converts JSON to model for API use
class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'name', 'location', 'last_triggered', 'last_image_url', 'owner_name', 'ip_address', 'is_active',
                  'has_sound', 'has_motion')
