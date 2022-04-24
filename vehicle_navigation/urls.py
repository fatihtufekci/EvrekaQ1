from django.urls import path
from vehicle_navigation import views as api_views

urlpatterns = [
    path('navigation-record/', api_views.get_vehicle_last_points, name="navigation-record"),
]
