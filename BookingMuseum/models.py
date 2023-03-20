from django.db import models
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from creditcards.models import CardNumberField, CardExpiryField
from django_countries.fields import CountryField
from django.db.models import Sum
# Create your models here.



class Credit(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    number = CardNumberField(max_length=20,null=True,blank=True)
    expire_date = CardExpiryField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
#class User_Info(models.Model):
    
    
class User(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = PhoneField(max_length=255,null=True,blank=True)
    post_code = models.CharField(max_length=6,null=True,blank=True)
    country = CountryField(max_length=255,null=True,blank=True)
    credit = models.OneToOneField(Credit, related_name='credit_info', on_delete= models.CASCADE)

    def __str__(self) -> str:
            return self.name

class Ticket_Reservation(models.Model): 
    TYPE_CHOICES =(
        ('Egyptian_Citizen','Egyptian_Citizen(20)'),
        ('Egyptian_Student','Egyptian_Student(5)'),
        ('Foreign_Visitor','Foreign_Visitor(100)'),
        ('Foreign_Student','Foreign_Student(50)'),
        ('photographic_camera','photographic_camera(50)'), 
    )
    type = models.CharField(max_length=255, choices = TYPE_CHOICES,null=True, blank=True)
    price = models.DecimalField(max_digits= 20, decimal_places=2,default=20)
    tickets_number = models.PositiveSmallIntegerField(null=True,blank=True)
    user = models.ForeignKey(User, related_name='Museum_Ticket_Reservation', on_delete= models.PROTECT) 
    if type == 'Egyptian_Citizen':
        price = 20
    
    elif type == 'Egyptian_Student':
        price = 5

    elif type == 'Foreign_Visitor':
         price = 100
         
    elif type == 'Foreign_Student':
        price = 50

    elif type == 'photographic_camera':
         price = 50
'''
    def  total_price(self):
        return (self.price * self.tickets_number)
    
    
    def __str__(self):
        return str(self.total_price)

'''    
def __str__(self):
    return str(self.price)   

    