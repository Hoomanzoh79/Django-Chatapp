from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from .users import CustomUser


class Profile(models.Model):
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="profile")
    # image = models.ImageField()
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=255, unique=True,blank=True)
    phone_number = models.CharField(max_length=12,
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")],
                                    unique=True,
                                    blank=True,
                                    )
    bio = models.CharField(max_length=300)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'profile : {self.username}'
    