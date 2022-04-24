from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vehicle_navigation.api.urls')),
    path('', include('vehicle_navigation.urls'))
]
