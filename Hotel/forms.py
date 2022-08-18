from multiprocessing.sharedctypes import Value
from django import forms
from django.forms import ModelForm
from .models import WorkWithUs


class FinishPaymentForm(forms.Form):
    paid_by = forms.CharField(label='Paid by', max_length=100)
    transactionid = forms.CharField(label='Transaction ID', max_length=100)
    
class BookingForm(forms.Form):
    hotel = forms.CharField(label='Hotel', max_length=100)
    # room = forms.CharField(label='Room', max_length=100)
    check_in= forms.DateField(label='Check In')
    check_out= forms.DateField(label='Check Out')
    quantity = forms.CharField(label='Quantity', max_length=100)
    
class WorkWithUsForm(ModelForm):
    class Meta:
        model=WorkWithUs
        fields='__all__'
        
# class CreateUserForm(ModelForm):
#     class Meta:
#         model=User
#         fields=['username', 'email', 'phone_number']