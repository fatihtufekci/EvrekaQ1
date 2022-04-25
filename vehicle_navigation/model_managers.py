from django.db import models
from django.utils import timezone


class NavigationRecordManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_last_points(self):
        return super().get_queryset().select_related('vehicle').filter(
            datetime__gt=timezone.now() - timezone.timedelta(2)).order_by(
                'vehicle', '-datetime').distinct('vehicle')