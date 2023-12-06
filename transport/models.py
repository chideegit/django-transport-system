from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class RouteFromOshodi(models.Model):
    route_choices = (
        (1, 'Oshodi'), 
        (2, 'Cele Exp.'), 
        (3, 'Ajah'),
        (4, 'Lekki'), 
        (5, 'Festac'), 
        (6, 'Ojota')
    )
    pick_up = models.CharField(max_length=10, choices=route_choices, default='Oshodi')
    destination = models.CharField(max_length=10, choices=route_choices)
    trip = models.CharField(
        max_length=20, 
        choices=(
            (1, 'One way'), 
            (2, 'Two way')
        ), 
        default='Two way'
    )


class Booking(models.Model):
    pass 
