# from tkinter import CASCADE
import email
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User

# Create your models here.


    
class City(models.Model):
    name = models.CharField(max_length=55)
 
    region=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Hotel(models.Model):
    city= models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=255)
    Specificlocation_or_subcity=models.CharField(max_length=255)
    description=models.TextField()
    star=models.PositiveIntegerField()
    number_of_room= models.PositiveIntegerField()
    image=models.ImageField(null=True, blank=True)
    admin= models.ForeignKey(User, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name


class HotelAdmin(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_admin")
    
    def __str__(self):
        return self.hotel.name

class Facilities(models.Model):
    type=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    hotel = models.ManyToManyField(Hotel)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type



    
class PaymentMethods(models.Model):
    
    name=models.CharField(max_length=255)
    #logo=
    type=models.CharField(max_length=255)
    service_number=models.CharField(max_length=255)
    payment_step=models.TextField()
    customer_service=models.PositiveIntegerField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
 
class PaymentInformations(models.Model):
    # payment_method=models.ForeignKey(PaymentMethods, on_delete=models.SET_NULL, null=True)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    method=models.CharField(max_length=255)
    service_number=models.CharField(max_length=255)
    account_or_shortcode=models.PositiveIntegerField()
    account_or_shortcode_holder=models.CharField(max_length=255)
    phone_number=models.PositiveIntegerField()
    customer_service=models.PositiveIntegerField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    

class RoomGroup(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type=models.CharField(max_length=255)
    room_photo=models.ImageField(null=True, blank=True)
    facility=models.CharField(max_length=200)
    number_of_bed=models.PositiveIntegerField()
    max_people= models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.PositiveIntegerField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.type

class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # hotel=models.CharField(max_length=255)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
  
    room=models.ForeignKey(RoomGroup, on_delete=models.CASCADE, null=True)
   
    check_in=models.DateField(null=True)
    check_out=models.DateField(null=True)
    quantity=models.PositiveIntegerField(null=True)
    # status=
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.room.type)
    
class BookingRoomNumber(models.Model):
     booking=models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True, related_name="booking_roomnumber")
     room_number=models.CharField(max_length=100)
     
     def __str__(self):
        return self.room_number
        
    
class FinishPayment(models.Model):
    booking=models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True, related_name="finishpymnt_booking")
    payment_method=models.ForeignKey(PaymentInformations, on_delete=models.CASCADE)
    paid_by=models.CharField(max_length=255, null=True)
    transactionid=models.CharField(max_length=255, null=True)
    # screenshot=
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.paid_by

class FnishPaymentStatus(models.Model):
    fnishpayment=models.OneToOneField(FinishPayment, on_delete=models.CASCADE, primary_key=True, related_name="finishpayment_status")
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.finishpayment
   
class BookingStatus(models.Model):
    booking=models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True, related_name="booking_status")
    accept=models.BooleanField(default=False)
    
    def str(self):
        return self.accept
    
class WorkWithUs(models.Model):
    full_name=models.CharField(max_length=255)
    phone_number=models.PositiveIntegerField()
    email=models.EmailField()
    hotel_name=models.CharField(max_length=255)
    hotel_address=models.CharField(max_length=255)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotel_name