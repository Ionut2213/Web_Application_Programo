from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pacient(models.Model):
    gender_option = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    location_option = [
        ('L', 'Location'),
        ('C', 'Call')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=gender_option)
    location = models.CharField(max_length=50, choices=location_option)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

    def get_full_name(self):
        return self.full_name()
    

class HistoryPacient(models.Model):
    message = models.JSONField()
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message