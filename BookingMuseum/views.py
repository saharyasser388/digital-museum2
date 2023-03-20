from django.shortcuts import render
from django.db.models import Sum
from .models import Ticket_Reservation
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
'''
def total_price():
        return (Ticket_Reservation.price * Ticket_Reservation.tickets_number)
'''

# Create your views here.
@api_view(['GET'])
def getBookingMuseum(request):
    return Response()