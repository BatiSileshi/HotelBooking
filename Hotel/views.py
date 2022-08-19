# from multiprocessing import context
from crypt import methods

from multiprocessing import context
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse

from .models import BookingRoomNumber,  Hotel, City, PaymentInformations, RoomGroup, Booking, PaymentMethods, FinishPayment
from .forms import  WorkWithUsForm
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.



def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    hotels=Hotel.objects.filter(
        Q(city__name__icontains=q) |
        Q(name__icontains=q)
        )
    
    cities=City.objects.all()
    context={'hotels': hotels, 'cities':cities}
    return render(request, 'Hotel/home.html', context)


def hotel(request, pk):
    hotel=Hotel.objects.get(id=pk)
    roomgroups=hotel.roomgroup_set.all()
    facilities=hotel.facilities_set.all()
    context = {'hotel':hotel, 'roomgroups':roomgroups, 'facilities':facilities}
    return render(request, 'Hotel/hotel.html', context)


def room(request, pk):
    roomgroup=RoomGroup.objects.get(id=pk)
    hotels=Hotel.objects.all()
    context={'roomgroup':roomgroup, 'hotels':hotels}
    return render(request, 'Hotel/room.html', context)

@unauthenticated_user
def loginPage(request):
    page='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
             user=User.objects.get(username=username)
          
        except:
            messages.error(request, 'Sorry! User does not exist.')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('admin-home')
        else :
          messages.error(request, 'Sorry! phone_number or password does not exist.')  
    context={'page':page}
    return render(request, 'Hotel/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

@unauthenticated_user
def registerPage(request):
    page='register'
    form=UserCreationForm()
    
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            
            group=Group.objects.get(name='customers')
            user.groups.add(group)
            
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
    context={'page':page, 'form':form}
    return render(request, 'Hotel/login_register.html', context)

@login_required(login_url='login')
def booking(request, pk):
    roomgroup=RoomGroup.objects.get(id=pk)
    user=User.objects.all()
    hotels=Hotel.objects.all()
    
    bookings=roomgroup.booking_set.all()
    
    if request.method=='POST':
        book=Booking.objects.create(
        user=request.user,
        hotel=roomgroup.hotel,
        
        room=roomgroup,
        
        check_in=request.POST['check_in'],
        check_out=request.POST['check_out'],
        quantity=request.POST['quantity']
        )
        return redirect ('my-booking', pk=request.user.id)
        
    context={'roomgroup':roomgroup, 'hotels':hotels, 'bookings':bookings, 'user':user}
    return render(request, 'Hotel/booking.html', context)

# def payment(request, pk):
#      roomgroup=RoomGroup.objects.get(id=pk)
#      hotels=Hotel.objects.all()
#      pymntinfos=PaymentInformations.objects.all()
#      context={'roomgroup':roomgroup, 'hotels':hotels, 'pymntinfos':pymntinfos}
#      return render(request, 'Hotel/pymnt.html', context)
 
def pymntInfo(request, pk):
    hotel=Hotel.objects.get(id=pk)
    infos=hotel.paymentinformations_set.all()
    # methods=PaymentMethods.objects.all()
    context={'hotel':hotel, 'infos':infos,  'methods':methods}
    return render(request, 'Hotel/infos.html', context)

@login_required(login_url='login')
def myBooking(request, pk):
    user=User.objects.get(id=pk)
    bookings=user.booking_set.filter().order_by('-created')
    roomnumber=BookingRoomNumber.objects.filter()

    # roomgroup=bookings.roomgroup_set.all()
    # books=Booking.objects.filter()
    context={'user':user, 'bookings':bookings, 'roomnumber':roomnumber}
    
    if request.user != user:
           return HttpResponse("You are not allowed here!")
    return render(request, 'Hotel/my-booking.html', context)



def getFinishPymnt(request, pk):

    booking=Booking.objects.get(id=pk)
    user=User.objects.all()
    roomgroups=RoomGroup.objects.all()
    payment_methods=booking.hotel.paymentinformations_set.all()
   
 
    if request.method == 'POST':
        finishpymnt=FinishPayment.objects.create(
        booking=booking,
        payment_method_id=request.POST['payment_method'],
        paid_by=request.POST['paid_by'],
        transactionid=request.POST['transactionid'],
        )
        return redirect ('home')
    context={'booking':booking, 'user':user, 'roomgroups':roomgroups, 'payment_methods':payment_methods}
    return render(request, 'Hotel/finish-pymnt.html', context)

def workWithUs(request):
    
    form=WorkWithUsForm()
    
    if request.method == 'POST':
        form =WorkWithUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form}
    return render(request, 'Hotel/workwithus_form.html', context)