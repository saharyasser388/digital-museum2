from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.User_Info)
admin.site.register(models.Museum_Ticket_Reservation)
admin.site.register(models.Credit)