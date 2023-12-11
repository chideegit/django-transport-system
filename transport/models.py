from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Route(models.Model):
    route_choices = (
        ('Oshodi', 'Oshodi'), 
        ('Cele Exp.', 'Cele Exp.'), 
        ('Ajah', 'Ajah'),
        ('Lekki', 'Lekki'), 
        ('Festac', 'Festac'), 
        ('Ojota', 'Ojota')
    )
    name = models.CharField(max_length=20)
    pickup = models.CharField(max_length=10, choices=route_choices, default='Oshodi')
    destination = models.CharField(max_length=10, choices=route_choices)
    trip = models.CharField(
        max_length=20, 
        choices=(
            ('One way', 'One way'), 
            ('Two way', 'Two way')
        ),
        default='Two way'
    )
    start_time = models.CharField(
        max_length=15, 
        choices=(
            ('07:00', '07:00'), 
            ('08:00', '08:00'), 
            ('12:00', '12:00'), 
            ('13:00', '13:00'), 
            ('17:00', '17:00'),
        )
    )

    def __str__(self):
        return self.name
