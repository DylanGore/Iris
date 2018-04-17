from django.contrib import admin
from django.urls import include, path
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
