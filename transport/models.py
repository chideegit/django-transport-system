from django.db import models
from django.contrib.auth import get_user_model
from bus.models import Bus

User = get_user_model()

class Route(models.Model):
    route_choices = (
        (1, 'Oshodi'), 
        (2, 'Cele Exp.'), 
        (3, 'Ajah'),
        (4, 'Lekki'), 
        (5, 'Festac'), 
        (6, 'Ojota')
    )
    pickup = models.CharField(max_length=10, choices=route_choices, default='Oshodi')
    destination = models.CharField(max_length=10, choices=route_choices)
    trip = models.CharField(
        max_length=20, 
        choices=(
            (1, 'One way'), 
            (2, 'Two way')
        ),
        default='Two way'
    )
    start_time = models.TimeField()


class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
     
