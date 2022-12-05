from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    grado_parentesco=models.IntegerField()
    fecha_nacimiento=models.CharField(max_length=50)