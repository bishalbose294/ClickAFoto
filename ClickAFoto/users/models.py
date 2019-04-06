from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class Photographers(models.Model):
    
    PhotographerID = models.AutoField(primary_key = True)
    username = models.CharField(unique = True, max_length = 15, null = False, blank = False)
    EmailID = models.EmailField(unique = True, null = False, blank = False)
    FirstName = models.CharField(max_length = 50, null = False, blank = False)
    MiddleName = models.CharField(max_length = 50, blank = True, null = True)
    LastName = models.CharField(max_length = 50, null = False, blank = False)
    DOB = models.DateField(null = False, blank = False)
    Gender = models.CharField(max_length = 1, null = False, blank = False)
    MobileNo = models.CharField(max_length = 10, null = False, blank = False)
    Nationality = models.CharField(max_length = 30, null = False, blank = False)
    AddressLine1 = models.TextField(max_length = 255, null = False, blank = False)
    AddressLine2 = models.TextField(max_length = 255, blank = True, null = True)
    AddressLine3 = models.TextField(max_length = 255, blank = True, null = True)
    Pincode = models.CharField(max_length = 6, null = False, blank = False)
    Bio = models.TextField(max_length = 500, null = False, blank = False)
    Timestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.username + " - " + self.FirstName + " - " + self.LastName + " - " + self.Bio
    
    def get_absolute_url(self):
        return reverse('users:users-detail', kwargs={'pk': self.PhotographerID})
    


class LoginManager(BaseUserManager):
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name = extra_fields['first_name'],
            last_name = extra_fields['last_name']
            )
        
        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, email, password, first_name, last_name):
        
        user = self.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class Login (AbstractUser):
    
    username = models.CharField(unique = True, max_length = 15, null = False, blank = False)
    password = models.CharField(max_length = 500,null = False, default="password123", blank = False) #password field will be defined in forms.py for Model Form
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
    email = models.EmailField(unique = True, null = False, blank = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now = True)
    last_login = models.DateTimeField(null = True)
    SQ1 = models.CharField(max_length = 100)
    SA1 = models.CharField(max_length = 100)
    SQ2 = models.CharField(max_length = 100)
    SA2 = models.CharField(max_length = 100)
    SQ3 = models.CharField(max_length = 100)
    SA3 = models.CharField(max_length = 100)
    

    objects = LoginManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email']
    
    def __str__(self):
        return self.username + " - " + self.LastLoginTimestamp
    

class Statistics (models.Model):
    
    Hitcounter = models.IntegerField()
    Users = models.IntegerField()
    Photos = models.IntegerField()
    Comments = models.IntegerField()
    Contests = models.IntegerField()
    Likes = models.IntegerField()
    Rating = models.IntegerField()
    Participants = models.IntegerField()
    Day = models.IntegerField()
    Month = models.IntegerField()
    Year = models.IntegerField()
    
    def __str__(self):
        return "Please view from Database Table Statistics"