from django.urls import path
from . import views

urlpatterns= [
    
    path('home/', views.startHome, name="start-home"),
    path('home/<str:pk>/', views.home, name="hoteladmin-home"),
    path('booked/<str:pk>/', views.booked, name="booked"),
    path('manage-room/<str:pk>/', views.manageRoomGroup, name="manage-room"),
    path('add-room/<str:pk>/', views.addRoomGroup, name="add-room"),
    path('update-room/<str:pk>/', views.updateRoomGroup, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    path('aceptdecline/<str:pk>/', views.acceptDecline, name="aceptdecline"),
    path('paidunpaid/<str:pk>/', views.finishPaymentStatus, name="paidunpaid"),
    path('booking/<str:pk>/assign-roomnumber', views.bookingRoomNumber, name="assign-roomnumber"),
    
    
]