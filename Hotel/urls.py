from django.urls import path
from . import views
from django.urls import include

urlpatterns= [
    path('', views.home, name="home"),
    path('work-with-us/', views.workWithUs, name="work-with-us"),
    path('hotel/<str:pk>/', views.hotel, name="hotel"),
    # path('hotel-room/<str:pk>/', views.room, name="room"),
    path('hotel-room/<str:pk>/booking', views.booking, name="booking"),
    # path('booking/<str:pk>/pymnt', views.payment, name="pymnt"),
    path('pymnt/<str:pk>/info', views.pymntInfo, name="info"),
    path('my-booking/<str:pk>/', views.myBooking, name="my-booking"),
    path('booking/<str:pk>/pymnt', views.getFinishPymnt, name="finish-pymnt"),
    
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

]