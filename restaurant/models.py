from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[
        MaxValueValidator(999999),
        MinValueValidator(0),
    ])
    
    def __str__(self):
        return f"{self.title} | {self.price}"
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[
        MaxValueValidator(30),
        MinValueValidator(1),
    ])
    booking_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return f"{self.name} | party of {self.no_of_guests}"