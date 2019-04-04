from django.db import models

# Create your models here.

class Photographers(models.Model):
    
    PhotographerID = models.PositiveIntegerField(primary_key = True)
    UserName = models.TextField(unique = True, max_length = 15, null = False)
    EmailID = models.EmailField(unique = True, null = False)
    FirstName = models.TextField(max_length = 50, null = False)
    MiddleName = models.TextField(max_length = 50)
    LastName = models.TextField(max_length = 50, null = False)
    DOB = models.DateField(null = False)
    Age = models.IntegerField(null = False)
    Gender = models.TextField(max_length = 1, null = False)
    MobileNo = models.IntegerField(null = False)
    Nationality = models.TextField(max_length = 30, null = False)
    AddressLine1 = models.TextField(max_length = 255, null = False)
    AddressLine2 = models.TextField(max_length = 255)
    AddressLine3 = models.TextField(max_length = 255)
    Pincode = models.IntegerField(null = False)
    Bio = models.TextField(max_length = 500, null = False)
    Timestamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.UserName + " - " + self.FirstName + " - " + self.LastName + " - " + self.Bio
    
    

class Login (models.Model):
    
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE)
    UserName = models.TextField(unique = True, max_length = 15, null = False)
    Password = models.TextField(max_length = 32, null = False) #Password field will be defined in forms.py for Model Form
    SQ1 = models.TextField(max_length = 100, null = False)
    SA1 = models.TextField(max_length = 100, null = False)
    SQ2 = models.TextField(max_length = 100, null = False)
    SA2 = models.TextField(max_length = 100, null = False)
    SQ3 = models.TextField(max_length = 100, null = False)
    SA3 = models.TextField(max_length = 100, null = False)
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