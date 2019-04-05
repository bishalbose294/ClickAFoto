from django.db import models
from django.urls.base import reverse


# Create your models here.

class Photographers(models.Model):
    
    PhotographerID = models.AutoField(primary_key = True)
    UserName = models.CharField(unique = True, max_length = 15, null = False, blank = False)
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
    Timestamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.UserName + " - " + self.FirstName + " - " + self.LastName + " - " + self.Bio
    
    def get_absolute_url(self):
        return reverse('users:users-detail', kwargs={'pk': self.PhotographerID})
    

class Login (models.Model):
    
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE)
    UserName = models.CharField(unique = True, max_length = 15, null = False)
    Password = models.CharField(max_length = 32, null = False) #Password field will be defined in forms.py for Model Form
    SQ1 = models.CharField(max_length = 100, null = False)
    SA1 = models.CharField(max_length = 100, null = False)
    SQ2 = models.CharField(max_length = 100, null = False)
    SA2 = models.CharField(max_length = 100, null = False)
    SQ3 = models.CharField(max_length = 100, null = False)
    SA3 = models.CharField(max_length = 100, null = False)
    TimeStamp = models.DateTimeField(auto_now = True, null = False)
    LastLoginTimestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.UserName + " - " + self.LastLoginTimestamp
    


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