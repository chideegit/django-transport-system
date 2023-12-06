from django.db import models

class Bus(models.Model):
    manufacturer = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=10)
    seats = models.PositiveIntegerField(default=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.manufacturer} - {self.plate_number}'