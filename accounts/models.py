from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    # make unique later 
    phone_number = models.CharField(max_length=12, 
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")])
    bio = models.CharField(max_length=350,blank=True)
    