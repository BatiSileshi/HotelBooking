from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Hotel.models import  BookingRoomNumber, BookingStatus, FinishPayment, Booking, HotelAdmin, RoomGroup, Hotel, FnishPaymentStatus

from Systemadmin.forms import RoomGroupForm
from .decorators import  admin_only, allowed_user


# Create your views here.
@login_required(login_url='login')
@admin_only
def startHome(request):
     
   context={}
   return render(request, 'HotelAdmin/starthome.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def home(request, pk):
    user=User.objects.get(id=pk)
    hoteladmins=user.hoteladmin_set.filter()

    context={'hoteladmins':hoteladmins}
    if request.user != user:
           return HttpResponse("You are not allowed here!")
   
    return render(request, 'HotelAdmin/home.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def booked(request, pk):
   hotel=Hotel.objects.get(id=pk)
   bookings=hotel.booking_set.filter().order_by('-created') 
   finishpayment=FinishPayment.objects.filter()
   roomnumber=BookingRoomNumber.objects.filter()

   context={'hotel':hotel, 'bookings':bookings, 'finishpayment':finishpayment, 'roomnumber':roomnumber}
   if request.user != hotel.admin: 
           return HttpResponse("You are not allowed here!")
   return render(request, 'HotelAdmin/booked.html', context)
   

@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def manageRoomGroup(request, pk):
    hotel=Hotel.objects.get(id=pk)
    roomgroups=hotel.roomgroup_set.all()

    context={'hotel':hotel, 'roomgroups':roomgroups}
    if request.user != hotel.admin:
           return HttpResponse("You are not allowed here!")
    
    return render(request, 'HotelAdmin/hotelroom.html', context)
       
@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def addRoomGroup(request, pk):
    hotel=Hotel.objects.get(id=pk)
    roomgroups=hotel.roomgroup_set.all()
    form=RoomGroupForm()
    
    if request.method == 'POST':
        
       roomgroup=RoomGroup.objects.create(
          hotel=hotel,
          type=request.POST['type'], 
          facility=request.POST['facility'], 
          number_of_bed=request.POST['number_of_bed'], 
          max_people=request.POST['max_people'], 
          price=request.POST['price'],
          quantity=request.POST['quantity'],  
          
       )
    
       return redirect('manage-room', pk=hotel.id)
        
    context={'form':form, 'roomgroups':roomgroups, 'hotel':hotel}
    
    if request.user != hotel.admin:
           return HttpResponse("You are not allowed here!")
    return render(request, 'HotelAdmin/roomgroup_form.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def updateRoomGroup(request, pk):
    roomgroups=RoomGroup.objects.get(id=pk)
   #  obj= get_object_or_404(RoomGroup, id=pk)
    
    
    if request.method == 'POST':
        
       roomgroup=RoomGroup.objects.filter(id=pk).update(
          hotel=roomgroups.hotel,
          type=request.POST['type'], 
          facility=request.POST['facility'], 
          number_of_bed=request.POST['number_of_bed'], 
          max_people=request.POST['max_people'], 
          price=request.POST['price'],
          quantity=request.POST['quantity'],  
          
       )
    
       return redirect('manage-room', pk=roomgroups.hotel.id)
    
    if request.user != roomgroups.hotel.admin: 
           return HttpResponse("You are not allowed here!")
    context={'roomgroups':roomgroups}
    return render(request, 'HotelAdmin/roomgroupedit_form.html', context)


@login_required(login_url='login')  
@allowed_user(allowed_roles=['hoteladmin'])     
def deleteRoom(request, pk):
    roomgroup=RoomGroup.objects.get(id=pk)
    if request.method=='POST':
       roomgroup.delete()
       return redirect('manage-room', pk=roomgroup.hotel.id)
    
    if request.user != roomgroup.hotel.admin: 
           return HttpResponse("You are not allowed here!")
    
    return render(request, 'HotelAdmin/delete.html', {'obj':roomgroup})



@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def bookingRequest(request, pk):
   hotel=Hotel.objects.get(id=pk)
   bookings=hotel.booking_set.filter().order_by('-created') 
   finishpayment=FinishPayment.objects.filter()

   context={'hotel':hotel, 'bookings':bookings, 'finishpayment':finishpayment}
   if request.user != hotel.admin: 
           return HttpResponse("You are not allowed here!")
   return render(request, 'HotelAdmin/booking_request.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def bookingRoomNumber(request, pk):
   booking=Booking.objects.get(id=pk)
   if request.method == 'POST':
        bookingroom=BookingRoomNumber.objects.create(
        booking=booking,
        room_number=request.POST['room_number'],
       
        )
        return redirect ('hoteladmin-home', pk=request.user.id)
   
   context={'booking':booking}
   if request.user != booking.hotel.admin: 
          return HttpResponse("You are not allowed here!")
        
   return render(request, 'HotelAdmin/assign-roomnumber.html', context)
       




@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def acceptDecline(request, pk):
   booking=Booking.objects.get(id=pk)
   
   if request.method == 'POST':
        accept=BookingStatus.objects.create(
        booking=booking,
        accept=request.POST['accept'],
       
        )
        return redirect ('hoteladmin-home', pk=request.user.id)
   
   context={'booking':booking}
   if request.user != booking.hotel.admin: 
           return HttpResponse("You are not allowed here!")
        
   return render(request, 'HotelAdmin/acceptdecline.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['hoteladmin'])
def finishPaymentStatus(request, pk):
   finishpayment=FinishPayment.objects.get(booking_id=pk)
   bookings=Booking.objects.filter()
   
   
   if request.method == 'POST':
        status=FnishPaymentStatus.objects.create(
        fnishpayment=finishpayment,
        status=request.POST['status'],
       
        )
        return redirect ('hoteladmin-home', pk=request.user.id)
   
   context={'bookings':bookings, 'finishpayment':finishpayment}
   if request.user != finishpayment.booking.hotel.admin: 
           return HttpResponse("You are not allowed here!")
   return render(request, 'HotelAdmin/paidunpaid.html', context)