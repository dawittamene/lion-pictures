from django.contrib import admin
from .models import *
from . import models




admin.site.register(Image)
admin.site.register(Gallary_Post)

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = ['First_Name', 'Mobile', 'Booking_for', 'Time_for', 'Booking_Date']
@admin.register(models.Contact)
class BookingAdmin(admin.ModelAdmin):
  list_display = ['Name', 'email', 'message',  'date_created']





