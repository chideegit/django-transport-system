from django import forms 
from .models import * 

class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'pickup', 'destination', 'trip', 'start_time']

class UpdateRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'