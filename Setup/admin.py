from django.contrib import admin
from Setup.models import clientes,Staff
from Depilacion.models import Zonas,Depilacion,Depilacion_zonas,Depilacion_staff


# Register your models here.
class ClientesAdmin (admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display= ['Nombre','Apellido','Telefono']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Nombre','Apellido']


class ZonasAdmin(admin.ModelAdmin):
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Zonas']

class StaffAdmin(admin.ModelAdmin):
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Asistente']

class Depilacion_zonas_Admin (admin.TabularInline):
    model = Depilacion_zonas
    extra = 1

class Depilacion_staff_Admin (admin.TabularInline):
    model = Depilacion_staff
    max_num = 1

class DepilacionAdmin (admin.ModelAdmin):
    inlines = [Depilacion_zonas_Admin,Depilacion_staff_Admin]
    extra = 1
    max_num = 1
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display= ['Cliente','foto_tipo','fecha']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Cliente__Nombre','fecha']
    list_filter = ['fecha']

admin.site.register(clientes,ClientesAdmin)
admin.site.register(Zonas,ZonasAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Depilacion,DepilacionAdmin)

