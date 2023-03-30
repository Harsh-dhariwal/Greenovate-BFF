from django import forms
from .models import comp_database




class carbon_emmision(forms.ModelForm):
    class Meta:
        model = comp_database
        fields = (
                  
                  )
