from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.

class clientes (models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=50, null=True,blank=True)
    Cuil = models.CharField(max_length=20, null=True,blank=True)
    Cumpleanos = models.DateField(null=True,blank=True)
    Activa = models.BooleanField(default=False)
    Observacion = models.TextField(max_length=140,null=True,blank=True)

    def __str__(self):
        return "%s,%s" % (self.Nombre,self.Apellido)

    class Meta:
        verbose_name = "Clientes"
        verbose_name_plural = "Clientes"
        ordering = ["Apellido"]

class Staff (models.Model):
    Asistente = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % (self.Asistente)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

