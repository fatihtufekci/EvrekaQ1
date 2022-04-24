from django.contrib import admin
from .models import NavigationRecord, Vehicle

admin.site.register(Vehicle)
admin.site.register(NavigationRecord)
