from django.db import models
from vehicle_navigation.model_managers import NavigationRecordManager


class Vehicle(models.Model):
    plate = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.plate}'



class NavigationRecord(models.Model):
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)

    objects = NavigationRecordManager()

    def __str__(self):
        return f'{self.datetime.strftime("%Y-%m-%d %H:%M:%S")} - {self.latitude} - {self.longitude} - {self.vehicle}'

