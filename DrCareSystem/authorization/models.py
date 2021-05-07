from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MyAccManager(BaseUserManager):
    def create_doctor_user(self,first_name,last_name,username,password,dr_license):
        user = self.create_user(
            username = username,
            dr_license = dr_license,
            first_name=first_name,
            last_name=last_name,
            password = password,
        )
        user.save(using=self._db)
        return user


class DrAccount(AbstractBaseUser):
    username                 = models.CharField( max_length=300,unique=True)
    first_name               = models.CharField(max_length=30, default='')
    last_name                = models.CharField(max_length=30, default='')
    dr_license               = models.IntegerField(max_length =8,unique=True)  
    objects = MyAccManager()
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username