from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-route/', add_route, name='add-route'), 
    path('update-route/<int:pk>/', update_route, name='update-route'), 
    path('all-routes/', all_routes, name='all-routes'), 
    path('buses-in-route/<int:pk>/', buses_in_route, name='buses-in-route')
]