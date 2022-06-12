from django.contrib import admin

# Register your models here.
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking, BookingAdmin)


