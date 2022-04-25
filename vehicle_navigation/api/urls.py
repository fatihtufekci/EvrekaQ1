from django.urls import path
from vehicle_navigation.api import views as api_views

urlpatterns = [
    path('navigation-record/', api_views.NavigationRecordViewSet.as_view({'get': 'list'})),

]