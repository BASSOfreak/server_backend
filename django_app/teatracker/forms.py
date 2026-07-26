from django import forms

from .models import Location, Entry, Item

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name',)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('location', 'items',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EntryForLocationForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('items',)
        
class ItemForLocationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name',)
