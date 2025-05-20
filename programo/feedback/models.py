from django.db import models
from django.contrib.auth.models import User
from pacienti.models import Pacient


# Create your models here.

class Feedback(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Feedback for {self.pacient} pe {self.session_date}'