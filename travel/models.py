from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100)
    signup_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    agency_id = models.ForeignKey(Agency, on_delete = (models.CASCADE))
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    agency_id = models.ForeignKey(Agency, on_delete= (models.CASCADE), null = True, blank= True)
    branch_id = models.ForeignKey(Branch, on_delete = (models.CASCADE), null = True, blank= True)
    id_card = models.CharField(max_length=100, null = True, blank= True)
    phone = models.CharField(max_length=100, null = True, blank= True)
    # gender = models.CharField(max_length=6)
    # gender = models.CharField(
    #     max_length=6,
    #     choices = [('MALE', 'MALE'), ('FEMALE', 'FEMALE')],
    #     null = True,
    #     blank= True
    # )
    
    REQUIRED_FIELDS = []


class Bus_layout(models.Model):
    nub_seats = models.CharField(max_length=100)
    layout = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nub_seats

class Bus(models.Model):
    Bus_layout_id = models.ForeignKey(Bus_layout, on_delete = (models.CASCADE))
    agency_id = models.ForeignKey(Agency, on_delete = (models.CASCADE))
    buy_type = models.CharField(max_length=100)
    bus_number = models.CharField(max_length = 100)
    nub_seats = models.CharField(max_length=100)


    def __str__(self):
        return self.bus_number



class Trip(models.Model):
    bus_id = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    driver_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    agency_id = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    from_origin = models.CharField(max_length=150)
    to_destination = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(auto_now_add=True)
    arrival_time = models.DateTimeField(auto_now_add=True, null = True)
    trip_cost = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=20)