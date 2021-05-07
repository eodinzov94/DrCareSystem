from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MyAccManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,password,dr_license):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username = username,
            dr_license = dr_license,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,password=None):
        user = self.create_user(
            username = username,
            first_name='Admin',
            last_name='Admin',
            password = password,
            dr_license = ""
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class DrAccount(AbstractBaseUser):
    data_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login               = models.DateTimeField(verbose_name='last login', auto_now=True,)
    is_admin                 = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)
    is_staff                 = models.BooleanField(default=False)
    is_superuser             = models.BooleanField(default=False)
    username                 = models.CharField(max_length=30,unique=True)
    first_name               = models.CharField(max_length=30, default='')
    last_name                = models.CharField(max_length=30, default='')
    dr_license               = models.CharField(max_length =8,unique=True)  
    objects = MyAccManager()
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True