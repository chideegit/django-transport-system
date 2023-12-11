from django.db import models
from django.contrib.auth import get_user_model
from transport.models import Route

User = get_user_model()

class Bus(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=10) 
    color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=10)
    seats = models.PositiveIntegerField(default=20)
    is_available = models.BooleanField(default=True)
    full_capacity = models.BooleanField(default=False)
    seats_remaining = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.manufacturer} - {self.plate_number}'
    
class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
     