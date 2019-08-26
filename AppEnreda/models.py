from django.db import models

# Create your models here.


class Creador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=35, null=True)
    def __str__(self):
        return self.nombre

task_choices = (
    ('Yes', 'YES'),
    ('No', 'NO'),
)

class CrudUser(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    end_date= models.DateField(blank=True, null=True)
    note=models.TextField(blank=True, null=True)
    adjunto = models.FileField(upload_to="archivos/", null=True, blank=True)
    creador=models.ManyToManyField(Creador)
    creador2 = models.CharField(max_length=30, blank=True, null=True)
    task=models.CharField(max_length=3, choices=task_choices)
    tag=models.CharField(max_length=30, blank=True)
    type=models.CharField(max_length=30, blank=True)