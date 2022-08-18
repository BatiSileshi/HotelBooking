from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
# from account.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import HotelForm, CityForm, FacilitiesForm, PaymentInformationsForm, PaymentMethodsForm, RoomGroupForm
from Hotel.models import  Hotel, City, Facilities, HotelAdmin, PaymentInformations, PaymentMethods, RoomGroup, WorkWithUs
from .decorators import allowed_user, admin_only
# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    users=User.objects.all()
    hotels=Hotel.objects.all()
    hotel_count=hotels.count()
    cities=City.objects.all()
    city_count=cities.count()
    facilities=Facilities.objects.all()
    pymentinfos=PaymentInformations.objects.all()
    pymntmethods=PaymentMethods.objects.all()
    roomgroups=RoomGroup.objects.all()
    context={'hotels':hotels, 'cities':cities, 'facilities':facilities, 'pymentinfos':pymentinfos, 
             'pymntmethods':pymntmethods, 
             'roomgroups':roomgroups,
             'hotel_count':hotel_count,
             'city_count':city_count,
             'users':users}
    return render(request, 'Admin/admin_home.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def manageUser(request):
    users=User.objects.all()
    groups=Group.objects.all()
   
    context={'users':users, 'groups':groups}
    return render(request, 'Admin/users.html', context)
    
@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def manageHotel(request):

    hotels=Hotel.objects.all()
    hotel_count=hotels.count()
    cities=City.objects.all()
    city_count=cities.count()
    facilities=Facilities.objects.all()
    pymentinfos=PaymentInformations.objects.all()
    pymntmethods=PaymentMethods.objects.all()
    roomgroups=RoomGroup.objects.all()
   
    context={ 'hotels':hotels, 'cities':cities, 'facilities':facilities, 'pymentinfos':pymentinfos, 
             'pymntmethods':pymntmethods, 
             'roomgroups':roomgroups,
             'hotel_count':hotel_count,
             'city_count':city_count}
    return render(request, 'Admin/manage-hotel.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def hotelRequest(request):
    workwithus=WorkWithUs.objects.all()
    context={'workwithus':workwithus}
    return render(request, 'Admin/hotel-request.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def manageCity(request):
    cities=City.objects.all()
    context={'cities':cities}
    return render(request, 'Admin/manage-city.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def manageAdmin(request):
    return render(request, 'Admin/manage-admin.html')


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def manageHotelAdmin(request):
    hoteladmins=HotelAdmin.objects.all()
    context={'hoteladmins':hoteladmins}
    return render(request, 'Admin/manage-hotel_admin.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addHotel(request):
    form=HotelForm()
    
    if request.method == 'POST':
        form =HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/hotel_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updateHotel(request, pk):
    hotel =Hotel.objects.get(id=pk)
    form =HotelForm(instance=hotel)
    
    if request.method=='POST':
        form=HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/hotel_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deleteHotel(request, pk):
    hotel=Hotel.objects.get(id=pk)
    if request.method=='POST':
       hotel.delete()
       return redirect('manage-hotel')
    
    return render(request, 'Admin/delete.html', {'obj':hotel})

#############     MANAGE CITY ##############
@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addCity(request):
    form=CityForm()
    
    if request.method == 'POST':
        form =CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/city_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updateCity(request, pk):
    city =City.objects.get(id=pk)
    form =CityForm(instance=city)
    
    if request.method=='POST':
        form=CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/city_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deleteCity(request, pk):
    city=City.objects.get(id=pk)
    if request.method=='POST':
       city.delete()
       return redirect('admin-home')
    
    return render(request, 'Admin/delete.html', {'obj':city})


#############     MANAGE FACILITIES ##############
@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addFacility(request):
    form=FacilitiesForm()
    
    if request.method == 'POST':
        form =FacilitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/facility_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updateFacility(request, pk):
    facility =Facilities.objects.get(id=pk)
    form =FacilitiesForm(instance=facility)
    
    if request.method=='POST':
        form=FacilitiesForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/facility_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deleteFacility(request, pk):
    facility=Facilities.objects.get(id=pk)
    if request.method=='POST':
       facility.delete()
       return redirect('admin-home')
    
    return render(request, 'Admin/delete.html', {'obj':facility})


#############     MANAGE PAYMENT INFORMATIONS ##############

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addPymntinfo(request):
    form=PaymentInformationsForm()
    
    if request.method == 'POST':
        form =PaymentInformationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/paymentinfo_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updatePymntinfo(request, pk):
    pymntinfo =PaymentInformations.objects.get(id=pk)
    form =PaymentInformationsForm(instance=pymntinfo)
    
    if request.method=='POST':
        form=PaymentInformationsForm(request.POST, instance=pymntinfo)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/paymentinfo_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deletePymntinfo(request, pk):
    pymntinfo=PaymentInformations.objects.get(id=pk)
    if request.method=='POST':
       pymntinfo.delete()
       return redirect('admin-home')
    
    return render(request, 'Admin/delete.html', {'obj':pymntinfo})

#############     MANAGE PAYMENT METHODS ##############

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addPymntmethod(request):
    form=PaymentMethodsForm()
    
    if request.method == 'POST':
        form =PaymentMethodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/pymentmethod_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updatePymntmethod(request, pk):
    pymntmethod =PaymentMethods.objects.get(id=pk)
    form =PaymentMethodsForm(instance=pymntmethod)
    
    if request.method=='POST':
        form=PaymentMethodsForm(request.POST, instance=pymntmethod)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/pymentmethod_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deletePymntmethod(request, pk):
    pymntmethod=PaymentMethods.objects.get(id=pk)
    if request.method=='POST':
       pymntmethod.delete()
       return redirect('admin-home')
    
    return render(request, 'Admin/delete.html', {'obj':pymntmethod})

#############     MANAGE ROOMGROUP ##############

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def addRoomGroup(request):
    form=RoomGroupForm()
    
    if request.method == 'POST':
        form =RoomGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/roomgroup_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def updateRoomGroup(request, pk):
    roomgroup =RoomGroup.objects.get(id=pk)
    form =RoomGroupForm(instance=roomgroup)
    
    if request.method=='POST':
        form=RoomGroupForm(request.POST, instance=roomgroup)
        if form.is_valid():
            form.save()
            return redirect('admin-home')
        
    context={'form':form}
    return render(request, 'Admin/roomgroup_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['systemadmin'])
def deleteRoomGroup(request, pk):
    roomgroup=RoomGroup.objects.get(id=pk)
    if request.method=='POST':
       roomgroup.delete()
       return redirect('admin-home')
    
    return render(request, 'Admin/delete.html', {'obj':roomgroup})




