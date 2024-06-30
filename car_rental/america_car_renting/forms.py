from django import forms 
from .models import * 


#Create an instance of ModelForm for simple demo of create Vehicle
class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields = '__all__'