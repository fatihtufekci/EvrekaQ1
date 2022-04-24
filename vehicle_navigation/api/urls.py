from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehicle_navigation.api import views as api_views

router = DefaultRouter()
router.register('navigation-record', api_views.NavigationRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]