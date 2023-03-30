from django import forms
from .models import Energy_generation

class Electricityform(forms.ModelForm):
    class Meta:
        model = Energy_generation
        fields = ('company_name','E_coal','E_hydro','E_nuclear','E_petroleum','E_wind','E_others')
