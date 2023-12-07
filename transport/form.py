from django import forms 
from .models import * 

class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

class UpdateRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'