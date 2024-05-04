from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Users(models.Model):
    ID = models.AutoField(primary_key=True)
    LOCATIONS = models.CharField(max_length=200)
    QRDECODE = models.CharField(max_length=200)

    def __str__(self):
        return self.ID
    
class Buses(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    start = models.TimeField()
    end = models.TimeField()
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ID
   
class AVK(models.Model):
    ID = models.AutoField(primary_key=True)
    Stop = models.CharField(max_length=100)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    def __str__(self):
        return self.ID
    
class SHABARI(models.Model):
    ID = models.AutoField(primary_key=True)
    Stop = models.CharField(max_length=100)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    def __str__(self):
        return self.ID
    
class COMOS(models.Model):
    ID = models.AutoField(primary_key=True)
    Stop = models.CharField(max_length=100)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    def __str__(self):
        return self.ID