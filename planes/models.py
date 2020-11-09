from django.db import models
from django.utils import timezone

# Create your models here.

class Plan(models.Model):
    NombrePlan = models.CharField(max_length=30)
    descripcion = models.TextField();
    precio = models.IntegerField();
    duracion = models.DateTimeField(default=timezone.now);
    
    def __str__(self):
        return self.NombrePlan