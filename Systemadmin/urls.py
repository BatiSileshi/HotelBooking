from django.urls import path
from . import views


urlpatterns= [
    path('home/', views.home, name="admin-home"),
    path('manage-hotel/', views.manageHotel, name="manage-hotel"),
    path('hotel-request/', views.hotelRequest, name="hotel-request"),
    path('manage-city/', views.manageCity, name="manage-city"),
    path('manage-admin/', views.manageAdmin, name="manage-admin"),
    path('manage-hotel_admin/', views.manageHotelAdmin, name="manage-hotel_admin"),
    path('users/', views.manageUser, name="manage-user"),
    
    path('add-hotel/', views.addHotel, name="add-hotel"),
    path('update-hotel/<str:pk>/', views.updateHotel, name="update-hotel"),
    path('delete-hotel/<str:pk>/', views.deleteHotel, name="delete-hotel"),
    
    path('add-city/', views.addCity, name="add-city"),
    path('update-city/<str:pk>/', views.updateCity, name="update-city"),
    path('delete-city/<str:pk>/', views.deleteCity, name="delete-city"),
    
    path('add-facility/', views.addFacility, name="add-facility"),
    path('update-facility/<str:pk>/', views.updateFacility, name="update-facility"),
    path('delete-facility/<str:pk>/', views.deleteFacility, name="delete-facility"),
    
    path('add-pymntinfo/', views.addPymntinfo, name="add-pymntinfo"),
    path('update-pymntinfo/<str:pk>/', views.updatePymntinfo, name="update-pymntinfo"),
    path('delete-pymntinfo/<str:pk>/', views.deletePymntinfo, name="delete-pymntinfo"),
    
    path('add-pymntmethod/', views.addPymntmethod, name="add-pymntmethod"),
    path('update-pymntmethod/<str:pk>/', views.updatePymntmethod, name="update-pymntmethod"),
    path('delete-pymntmethod/<str:pk>/', views.deletePymntmethod, name="delete-pymntmethod"),
    
    path('add-roomgroup/', views.addRoomGroup, name="add-roomgroup"),
    path('update-roomgroup/<str:pk>/', views.updateRoomGroup, name="update-roomgroup"),
    path('delete-roomgroup/<str:pk>/', views.deleteRoomGroup, name="delete-roomgroup"),
    
    
  
]
