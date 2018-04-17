from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register('cameras', views.CameraView)

urlpatterns = [
    path('', include(router.urls), name='index')
]
