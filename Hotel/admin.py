from django.contrib import admin
from .models import BookingRoomNumber, HotelAdmin, FnishPaymentStatus, BookingStatus,  Hotel, RoomGroup, City, PaymentInformations, PaymentMethods, Facilities, Booking, FinishPayment
# Register your models here.


admin.site.register(Hotel)
admin.site.register(RoomGroup)
admin.site.register(City)
admin.site.register(PaymentInformations)
admin.site.register(PaymentMethods)
admin.site.register(Facilities)
admin.site.register(Booking)
admin.site.register(FinishPayment)

admin.site.register(BookingStatus)
admin.site.register(FnishPaymentStatus)
admin.site.register(HotelAdmin)
admin.site.register(BookingRoomNumber)