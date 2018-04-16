from django.shortcuts import render, get_object_or_404

from .models import Camera


# Main View
def index(request):
    return render(request, 'devices/index.html', {})


# Devices List View - Manage
def manage_devices(request):
    all_cameras = Camera.objects.all()
    if request.user.is_authenticated:
        return render(request, 'devices/manage_devices.html', {'all_cameras': all_cameras})
    else:
        return render(request, 'users/unauthenticated.html')


# Devices List View - Monitoring
def monitor_devices(request):
    all_cameras = Camera.objects.all
    if request.user.is_authenticated:
        return render(request, 'devices/monitor_devices.html', {'all_cameras': all_cameras})
    else:
        return render(request, 'users/unauthenticated.html')


# Specific Camera Info
def manage_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    if request.user.is_authenticated:
        return render(request, 'devices/manage_camera.html', {'device': device})
    else:
        return render(request, 'users/unauthenticated.html')


# View Camera Feed Full Screen
def view_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    if request.user.is_authenticated:
        return render(request, 'devices/view_camera.html', {'device': device})
    else:
        return render(request, 'users/unauthenticated.html')

