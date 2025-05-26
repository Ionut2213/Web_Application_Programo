import random
from django.db import models

# Create your models here.


class RegisterVerificationRequestModel(models.Model):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    verification_code = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        self.verification_code = str(random.randint(100000, 999999))
        super(RegisterVerificationRequestModel, self).save(*args, **kwargs)
