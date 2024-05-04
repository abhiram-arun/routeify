from django.db import models

# Create your models here.

class Users(models.Model):
    ID = models.AutoField(primary_key=True)
    LOCATIONS = models.CharField(max_length=200)
    QRDECODE = models.CharField(max_length=200)

    def __str__(self):
        return self.ID
    
class Buses(models.Model):
    ID = models.AutoField(primary_key = True)
    FLAG = models.IntegerField();
    LOCATIONS = models.CharField(max_length=200)
    DENSITY = models.IntegerField()
    QRCODE = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ID