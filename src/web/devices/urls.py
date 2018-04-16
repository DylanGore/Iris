from django.urls import path, include

from . import views

app_name = 'devices'

urlpatterns = [
    path('', views.index, name='index'),
    path('manage/', views.manage_devices, name='manage_devices'),
    path('monitor/', views.monitor_devices, name='monitor_devices'),
    path('manage/camera/<int:device_id>/', views.manage_camera, name='manage_camera'),
    path('view/camera/<int:device_id>/', views.view_camera, name='view_camera'),
]