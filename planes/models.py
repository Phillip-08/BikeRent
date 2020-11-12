from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='/media/photos')
class Plan(models.Model):
    NombrePlan = models.CharField(max_length=30)
    descripcion = models.TextField();
    precio = models.IntegerField();
    duracion = models.DateTimeField(default=timezone.now);
    imagen = models.ImageField(upload_to="planes", null = True)
    
    def __str__(self):
        return self.NombrePlan