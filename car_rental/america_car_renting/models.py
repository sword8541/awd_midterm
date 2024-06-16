from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f'{self.state_name}'


class City(models.Model):
    city_name = models.CharField(max_length=128,null=False,blank=False)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'{self.city_name}'


class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=128,null=False,blank=False,db_index=True)  
    vehicle_model = models.CharField(max_length=128,null=False,blank=False)
    vehicle_make = models.CharField(max_length=128,null=False,blank=False) 
    vehicle_type = models.CharField(max_length=128,null=False,blank=False) 
    vehicle_year = models.CharField(max_length=128,null=False,blank=False)
    
    renter_trips_taken = models.IntegerField()
    review_count = models.IntegerField()
    rate_daily = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(5000)])
    #ranking within 1-5
    ranking = models.DecimalField(decimal_places=2,max_digits=3,validators=[MinValueValidator(1.00),MaxValueValidator(5.00)]) 
    fuel_type =  models.CharField(max_length=128,null=False,blank=False)  
    # a city can have many renting cars running
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'type: {self.vehicle_type} model: {self.vehicle_model} made by {self.vehicle_make}'

class Vehicle_renting(models.Model):
    owner_id = models.CharField(max_length=128,null=False,blank=False,db_index=True) 
    # a person can own several cars
    vehicle = models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING)
    

