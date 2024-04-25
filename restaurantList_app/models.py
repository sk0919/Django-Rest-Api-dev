from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Location(models.Model):
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    
    
    def __str__(self) -> str:
        return "state : "+ self.state + " & city : "  +self.city
    