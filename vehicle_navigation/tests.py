from django.test import TestCase
from vehicle_navigation.api.serializers import NavigationRecordSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from vehicle_navigation.models import NavigationRecord, Vehicle
import datetime

def populate_navigation_record_url():
    return reverse("vehicle-navigation:navigation-records")

class NavigationRecordApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @classmethod
    def setUpTestData(cls):
        cls.vehicle = Vehicle.objects.create(plate="34 ABC 000")
        cls.navigation_record = NavigationRecord.objects.create(
            latitude="34.34",
            longitude="34.34",
            vehicle = cls.vehicle,
            datetime = datetime.datetime(2022, 4, 25, 1, 7, 55, 744848)
        )
    
    def test_navigation_record(self):
        navigation_record = NavigationRecord(
            latitude="34.34",
            longitude="34.34",
            vehicle = self.vehicle,
            datetime = datetime.datetime(2022, 4, 25, 1, 7, 55, 744848)
        )
        self.assertEqual(navigation_record.latitude, "34.34")
        self.assertEqual(navigation_record.longitude, "34.34")
        self.assertEqual(navigation_record.vehicle.plate, self.vehicle.plate)
        self.assertEqual(navigation_record.datetime, datetime.datetime(2022, 4, 25, 1, 7, 55, 744848))
    

    def test_access_navigation_record_url(self):
        res = self.client.get("http://localhost:8000/api/navigation-record/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_navigation_record_api(self):
        res = self.client.get(populate_navigation_record_url())

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(NavigationRecord.objects.all().count(), 1)
    
    def test_get_last_points(self):
        old_navigation_record = NavigationRecord(
            latitude="34.34",
            longitude="34.34",
            vehicle = self.vehicle,
            datetime = datetime.datetime(2022, 4, 20, 1, 7, 55, 744848)
        )
        self.assertEqual(NavigationRecord.objects.get_last_points().count(), 1)


class VehicleModelTest(TestCase):
    def test_vehicle(self):
        vehicle = Vehicle.objects.create(plate="34 XYZ 000")
        self.assertEqual(vehicle.plate, "34 XYZ 000")
        self.assertEqual(Vehicle.objects.all().count(), 1)