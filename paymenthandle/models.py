from django.db import models
import datetime 
from hotel.models import Hotel


class Payment(models.Model):
    
    payment_option_choices = [
        ('cash','Cash'),
        ('bkash', 'Bkash'),
        ('rocket', 'Rocket'),
        ('mastercard', 'Mastercard'),
    ]
    
    room_type_choices = [
        ('NAC', 'Non AC'),
        ('YAC', 'AC'),
        ('DEL', 'Deluxe'),
        ('KIN', 'King'),
        ('QUE', 'Queen'),
    ]

    name=models.CharField(max_length=40,null=False, blank=False)
    payment_option = models.CharField(max_length=20, choices=payment_option_choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = models.DateField(null=True , blank=True)
    num_rooms = models.IntegerField()
    payment_option_image = models.URLField(blank=True)


    cvv = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    promo_code=models.CharField(max_length=15,null=True,blank=True)
    room_type=models.CharField(max_length=5, choices=room_type_choices)
    check_in=models.DateTimeField(blank=True, null=True)
    check_out=models.DateTimeField(blank=True, null=True)
    
   
  
    

    def __str__(self):
        return f"{self.payment_option} - {self.amount}"

