from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    last_active = models.DateTimeField('last active')
    last_image_url = models.CharField(max_length=256)
    owner_name = models.CharField(max_length=64)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    is_active = models.BooleanField(default=True)
    has_sound = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '[' + self.location + ']'


class MotionDetector(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    last_triggered = models.DateTimeField('last triggered')
    url = models.URLField(max_length=512, default="127.0.0.1")
    owner_name = models.CharField(max_length=64)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    is_active = models.BooleanField(default=False)
