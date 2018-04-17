from rest_framework import serializers
from devices.models import Camera


# Converts JSON to model for API use
class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'name', 'location', 'last_triggered', 'last_image_url', 'owner_name', 'ip_address', 'is_active',
                  'has_sound', 'has_motion')
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'owner_name': {'read_only': True},
            'has_sound': {'read_only': True},
            'has_motion': {'read_only': True}
        }
