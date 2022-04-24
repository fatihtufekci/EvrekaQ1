from django.db.models import fields
from rest_framework import serializers
from vehicle_navigation.models import NavigationRecord, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('plate')


class NavigationRecordSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()
    vehicle_plate = serializers.SerializerMethodField()

    class Meta:
        model = NavigationRecord
        fields = ('latitude', 'longitude', 'vehicle_plate', 'datetime')

    def get_datetime(self, obj):
        return f'{obj.datetime.strftime("%Y-%m-%d %H:%M:%S")}'
    
    def get_vehicle_plate(self, obj):
        return f'{obj.vehicle.plate}'