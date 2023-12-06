from django import forms 
from .models import * 

class AddBusForm(forms.ModelForm):
    class Meta:
        model = Bus 
        fields = '__all__'

class UpdateBusForm(forms.ModelForm):
    class Meta:
        model = Bus 
        fields = '__all__'