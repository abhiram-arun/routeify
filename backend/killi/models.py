from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    Location = models.TextField()
    
    def __str__(self):
        return self.name[0:50]
    class Meta:
        ordering = ['-name']
        
class Buses(models.Model):
    name = models.CharField(max_length=200)
    start = models.TimeField()
    end = models.TimeField()
    
    def __str__(self):
        return self.name[0:50]
    
    class Meta:
        ordering = ['-start']
        
class Bus1(models.Model):
    stop = models.CharField(max_length=200)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    
    def __str__(self):
        return self.stop[0:50]
    class Meta:
        ordering = ['-Time']
        
class Bus2(models.Model):
    stop = models.CharField(max_length=200)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    
    def __str__(self):
        return self.stop[0:50]
    class Meta:
        ordering = ['-Time']
        
class Bus3(models.Model):
    stop = models.CharField(max_length=200)
    Time = models.TimeField()
    Crowd = models.IntegerField(validators=[MaxValueValidator(100)])
    
    def __str__(self):
        return self.stop[0:50]
    class Meta:
        ordering = ['-Time']