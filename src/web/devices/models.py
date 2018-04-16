from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    last_triggered = models.DateTimeField(auto_now_add=True)
    last_image_url = models.CharField(max_length=256)
    owner_name = models.CharField(max_length=64)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    is_active = models.BooleanField(default=True)
    has_sound = models.BooleanField(default=False)
    has_motion = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '[' + self.location + ']'
