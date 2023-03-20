from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)

#admin.site.register(models.Ticket_Reservation)

admin.site.register(models.Credit)

@admin.register(models.Ticket_Reservation)
class Ticket_ReservationAdmin(admin.ModelAdmin):
   fields = ['type','price','tickets_number','user']
   list_display = ['user','type','tickets_number']
