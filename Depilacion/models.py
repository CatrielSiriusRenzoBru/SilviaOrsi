from django.db import models
from Setup.models import clientes,Staff

# Create your models here.

class Zonas (models.Model):
    Zona = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.Zona)

    class Meta:
        verbose_name = "Zonas"
        verbose_name_plural = "Zonas"

class Depilacion (models.Model):
    Cliente = models.ForeignKey(clientes,on_delete=models.SET_NULL,blank=True,null=True)
    FOTO_TIPO_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]
    foto_tipo = models.CharField( max_length = 1,
        choices=FOTO_TIPO_CHOICES,
        default=1,)
    fecha = models.DateTimeField()

class Depilacion_zonas (models.Model):
    Depilacion = models.ForeignKey(Depilacion, on_delete=models.SET_NULL, blank=True, null=True)
    Zona = models.ForeignKey(Zonas, on_delete=models.SET_NULL, blank=True, null=True)
    Potencia =models.IntegerField()

    class Meta:
        verbose_name = "Zonas"
        verbose_name_plural = "Zonas"

class Depilacion_staff (models.Model):
    Depilacion = models.ForeignKey(Depilacion, on_delete=models.SET_NULL, blank=True, null=True)
    asistente = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    Observacion = models.TextField(max_length=140, null=True, blank=True)

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistente"

class Reservas (models.Model):
    Cliente = models.ForeignKey(clientes, on_delete=models.SET_NULL, blank=True, null=True)
    Fecha_reserva = models.DateField()
    Hora_reserva = models.TimeField()