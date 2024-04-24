from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name