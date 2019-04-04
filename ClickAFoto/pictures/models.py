from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Photographers
from django.urls import reverse


# Create your models here.

class Pictures(models.Model):
    
    PictureID = models.PositiveIntegerField(primary_key = True)
    Name = models.TextField(unique = True, max_length = 50, null = False)
    Description = models.TextField(max_length = 500, null = False)
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE) #Primary key to be referenced from Photographer(PhotographerID)
    Location = models.TextField(max_length = 30, null = False)
    Keywords = models.TextField(max_length = 255, null = False)
    Views = models.IntegerField(default=0, null = False)
    Visibility = models.BooleanField(default = True, null = False)
    PhotoFile = models.FileField()
    Timestamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.Name + " - " + self.Description 
    
    def get_aboslute_url(self):
        return reverse('pictures:picturesIndex.html', kwargs={'pk': self.pk})



class Likes(models.Model):
    
    LikeID = models.PositiveIntegerField(primary_key = True)
    PictureID = models.ForeignKey(Pictures, on_delete=models.CASCADE) #Primary key to be referenced from PictureID(PictureID)
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE) #Primary key to be referenced from Photographer(PhotographerID)
    Value = models.BooleanField(default = True, null = False)
    Timestamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.PictureID.Name + " - " + self.PhotographerID.Name
    
    

class Comments(models.Model):
    
    CommentID = models.PositiveIntegerField(primary_key = True)
    Comments = models.TextField(max_length = 500, null = False)
    PictureID = models.ForeignKey(Pictures, on_delete=models.CASCADE) #Primary key to be referenced from PictureID(PictureID)
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE) #Primary key to be referenced from Photographer(PhotographerID)
    TimeStamp = models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.PictureID.Name + " - " + self.Comments + " - " + self.PhotographerID.Name 
    
    

class Ratings(models.Model):
    
    RatingID = models.PositiveIntegerField(primary_key = True)
    PictureID = models.ForeignKey(Pictures, on_delete=models.CASCADE) #Primary key to be referenced from PictureID(PictureID)
    PhotographerID = models.ForeignKey(Photographers, on_delete=models.CASCADE) #Primary key to be referenced from Photographer(PhotographerID)
    Value = models.IntegerField(default=1, null = False, validators=[MaxValueValidator(10), MinValueValidator(1)])
    Timestamp =  models.DateTimeField(auto_now = True, null = False)
    
    def __str__(self):
        return self.PictureID.Name + " - " + self.Value + " - " + self.PhotographerID.Name 
