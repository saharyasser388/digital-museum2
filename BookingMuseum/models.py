from django.db import models
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from creditcards.models import CardNumberField, CardExpiryField
from django_countries.fields import CountryField
# Create your models here.

class User_Info(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = PhoneField(max_length=255,null=True,blank=True)
    post_code = models.CharField(max_length=6,null=True,blank=True)
    country = CountryField(max_length=255,null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Credit(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    number = CardNumberField(max_length=20,null=True,blank=True)
    expire_date = CardExpiryField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    user_info = models.OneToOneField(User_Info, related_name='User', on_delete= models.CASCADE, primary_key= True)
    credit = models.OneToOneField(Credit, related_name='User_credit_info', on_delete= models.CASCADE)

class Museum_Ticket_Reservation(models.Model): 
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    tickets_number = models.PositiveSmallIntegerField(null=True,blank=True)
    user = models.ForeignKey(User, related_name='Museum_Ticket_Reservation', on_delete= models.PROTECT)   
