from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from .models import Camera


# Main View
def index(request):
    return render(request, 'devices/index.html', {})


# Devices List View - Manage
def manage_devices(request):
    # Show all cameras if user is an admin, otherwise show only devices belonging to a specific user
    if request.user.is_staff:
        all_cameras = Camera.objects.all()
    else:
        all_cameras = Camera.objects.filter(owner_name=request.user.username)

    if request.user.is_authenticated:
        return render(request, 'devices/manage_devices.html', {'all_cameras': all_cameras})
    else:
        raise PermissionDenied


# Devices List View - Monitoring
def monitor_devices(request):
    # Show all cameras if user is an admin, otherwise show only devices belonging to a specific user
    if request.user.is_staff:
        all_cameras = Camera.objects.all()
    else:
        all_cameras = Camera.objects.filter(owner_name=request.user.username)

    if request.user.is_authenticated:
        return render(request, 'devices/monitor_devices.html', {'all_cameras': all_cameras})
    else:
        raise PermissionDenied


# Specific Camera Info
def manage_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    if request.user.is_authenticated and (device.owner_name == request.user.username or request.user.is_staff):
        return render(request, 'devices/manage_camera.html', {'device': device})
    else:
        raise PermissionDenied


# View Camera Feed Full Screen
def view_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    if request.user.is_authenticated and (device.owner_name == request.user.username or request.user.is_staff):
        return render(request, 'devices/view_camera.html', {'device': device})
    else:
        raise PermissionDenied
