from django import forms

from .models import Location, Entry, Item

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('name',)
