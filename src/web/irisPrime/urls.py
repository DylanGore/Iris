from functools import partial

from django.conf.urls import handler403
from django.contrib import admin
from django.urls import include, path
from django.views.defaults import permission_denied, page_not_found, server_error, bad_request
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from irisPrime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', include('devices.urls'), name="devices"),
    path('users/', include('users.urls'), name="users"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls'), name="api"),
    path('api/auth/', include('rest_framework.urls'), name='api/auth'),
    path('api/token/', TokenObtainPairView.as_view(), name='api/token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='api/token/refresh'),
    path('', views.index, name='index'),
]

# Custom Error Pages
handler403 = partial(bad_request, template_name='devices/errors/400.html')
handler403 = partial(permission_denied, template_name='devices/errors/403.html')
handler404 = partial(page_not_found, template_name='devices/errors/404.html')
handler500 = partial(server_error, template_name='devices/errors/500.html')
