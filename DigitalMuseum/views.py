from BookingMuseum.models import Ticket_Reservation
from django.db.models import Sum

def total_price(request):
        total = Ticket_Reservation.objects.filter('Ticket_Reservation__User').aggregate(TOTAL = Sum('price'))['TOTAL']
        return total