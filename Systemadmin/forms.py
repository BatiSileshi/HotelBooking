from django.forms import ModelForm

from Hotel.models import Hotel, City, Facilities, PaymentInformations, PaymentMethods, RoomGroup

class HotelForm(ModelForm):
    class Meta:
        model=Hotel
        fields='__all__'
        # fileds=['name', 'body']   we can indetfy
        
class CityForm(ModelForm):
    class Meta:
        model=City
        fields='__all__'
        
class FacilitiesForm(ModelForm):
    class Meta:
        model=Facilities
        fields='__all__'
        
class PaymentInformationsForm(ModelForm):
    class Meta:
        model=PaymentInformations
        fields='__all__'
        
class PaymentMethodsForm(ModelForm):
    class Meta:
        model=PaymentMethods
        fields='__all__'
        
class RoomGroupForm(ModelForm):
    class Meta:
        model=RoomGroup
        fields='__all__'
        
