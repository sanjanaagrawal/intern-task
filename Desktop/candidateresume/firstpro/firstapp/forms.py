from django import forms
from .models import modeltable

class formtable(forms.ModelForm):
    class Meta():
        model=modeltable
        fields='__all__'
