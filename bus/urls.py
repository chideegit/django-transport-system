from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-bus/', add_bus, name='add-bus'), 
    path('update-bus/<int:pk>/', update_bus, name='update-bus'), 
    path('all-buses/', all_buses, name='all-buses')
]