from django import forms
from .models import Items


class Itemsform(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'done']