# Main View
from django.shortcuts import redirect


# Redirects the root url to the devices index
def index(request):
    return redirect('devices:index')
