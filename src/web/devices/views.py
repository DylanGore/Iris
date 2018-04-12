from django.shortcuts import render, get_object_or_404

from .models import Camera, MotionDetector


# Main View
def index(request):
    return render(request, 'devices/index.html', {})


# Devices List View - Manage
def manage_devices(request):
    all_cameras = Camera.objects.all()
    all_detectors = MotionDetector.objects.all()
    return render(request, 'devices/manage_devices.html', {'all_cameras': all_cameras, 'all_detectors': all_detectors})


# Devices List View - Monitoring
def monitor_devices(request):
    all_cameras = Camera.objects.all()
    all_detectors = MotionDetector.objects.all()
    return render(request, 'devices/monitor_devices.html', {'all_cameras': all_cameras, 'all_detectors': all_detectors})


# Specific Camera Info
def manage_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    return render(request, 'devices/manage_camera.html', {'device': device})


# Specific MotionDetector Info
def manage_detector(request, device_id):
    device = get_object_or_404(MotionDetector, id=device_id)
    return render(request, 'devices/manage_detector.html', {'device': device})


# View Camera Feed Full Screen
def view_camera(request, device_id):
    device = get_object_or_404(Camera, id=device_id)
    return render(request, 'devices/view_camera.html', {'device': device})