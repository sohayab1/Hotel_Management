from django.db import models
from django.conf import settings #user model from settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Hotel(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
   
    
    def __str__(self):
        return self.name
    

    
    
class Room(models.Model):
    
    Room_Categories=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    ) #left for database,Right to show
    
    number=models.IntegerField()
    category=models.CharField(max_length=3, choices=Room_Categories)
    beds=models.IntegerField()
    capacity=models.IntegerField()

    def __str__(self): #whenever you do something with your model it will show you this representation
        return f'{self.number}.{self.category} with {self.beds} beds for {self.capacity} people '


class Booking(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #settings have authUsermodel,
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

class Review(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating}"

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    


