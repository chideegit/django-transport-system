from django.urls import path 
from .views import * 

urlpatterns = [
    path('register-passenger/', register_passenger, name='register-passenger'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout')
]