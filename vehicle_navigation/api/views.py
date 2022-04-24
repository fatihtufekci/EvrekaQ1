from rest_framework import viewsets
from django.utils import timezone

from vehicle_navigation.api.serializers import NavigationRecordSerializer
from vehicle_navigation.models import NavigationRecord


class NavigationRecordViewSet(viewsets.ModelViewSet):
    queryset = NavigationRecord.objects.get_last_points()
    serializer_class = NavigationRecordSerializer