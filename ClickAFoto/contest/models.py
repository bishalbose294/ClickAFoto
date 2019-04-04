from django.db import models
from pictures.models import Pictures


# Create your models here.

class Categories(models.Model):
    
    CategoryID = models.PositiveIntegerField(primary_key = True)
    Name = models.TextField(max_length = 100, null = False)
    Description = models.TextField(max_length = 100, null = False)
    Count = models.IntegerField(null = False, default = 0)
    Timestamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.Name + " - " + self.Description
    
    

class Contests(models.Model):
    
    ContestID = models.PositiveIntegerField(primary_key = True)
    ContestName = models.TextField(max_length = 100, null = False)
    Description = models.TextField(max_length = 500, null = False)
    StartDate = models.DateField(null = False)
    EndDate = models.DateField(null = False)
    UploadStartDate = models.DateField(null = False)
    UploadEndDate = models.DateField(null = False)
    CategoryID = models.ForeignKey(Categories, on_delete=models.CASCADE) #Primary key to be referenced from ContestCategories(CategoryID)
    WinnerPictureID = models.ForeignKey(Pictures, on_delete=models.CASCADE) #Primary key to be referenced from Pictures(PictureID) 
    Timestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.ContestName + " - " + self.Description
    
    
class ContestRegisters(models.Model):
    ContestID = models.ForeignKey(Contests, on_delete=models.CASCADE) #Primary key to be referenced from Contests(ContestID)
    PictureID = models.ForeignKey(Pictures, on_delete=models.CASCADE) #Primary key to be referenced from Pictures(PictureID)
    Timestamp = models.DateTimeField(auto_now = True) 
    
    def __str__(self):
        return self.ContestID.ContestName + " - " + self.PictureID.Name + " - " + self.PhotographerID.UserName
    
    