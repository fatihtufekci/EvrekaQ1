from django.utils import timezone
from django.http import JsonResponse

from vehicle_navigation.models import NavigationRecord


def get_vehicle_last_points(request):

    queryset = NavigationRecord.objects.select_related('vehicle')
    
    last_points = list(queryset.filter(datetime__gt=timezone.now() - timezone.timedelta(2)).values('longitude','latitude','vehicle__plate','datetime').
                                order_by('vehicle', '-datetime').distinct('vehicle'))
    
    data = {
        'last_points': last_points
    }

    return JsonResponse(data)