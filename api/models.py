from django.db import models
from PIL import Image

# Creating models.
class Item(models.Model):
    Image= models.ImageField(null=True,blank=True)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Age=models.IntegerField(null=True)
    Location=models.CharField(max_length=50,null=True)
    Occupation=models.CharField(max_length=20,null=True,blank=True)
    Uploded_by=models.CharField(max_length=50,null=True,blank=True)
    Uploded_on=models.TimeField( auto_now_add=True,null=True)
    No_of_download=models.IntegerField(null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    # string representation of the class
    def __str__(self):
        #it will return the Firstname
        return self.Firstname
