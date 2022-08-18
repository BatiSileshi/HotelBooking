from django.forms import ModelForm

from Hotel.models import Hotel
from django import forms
from django.forms import ModelForm


# class UpdateRoomGroupForm(forms.Form):
#     hotel = forms.CharField(label='Hotel', max_length=100)
#     type = forms.CharField(label='Type', max_length=100)
#     facility = forms.CharField(label='Facility', max_length=100)
#     number_of_bed = forms.IntegerField(label='number_of_bed')
#     max_people = forms.IntegerField(label='max_people')
#     price = forms.IntegerField(label='price')
#     quantity = forms.IntegerField(label='quantity')