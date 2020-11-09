from django.db import models

# Create your models here.

class Plan(models.Model):
    NombrePlan = models.CharField(max_length=30)
    descripcion = models.TextField();
    precio = models.IntegerField();
    
    def __str__(self):
        return self.NombrePlan