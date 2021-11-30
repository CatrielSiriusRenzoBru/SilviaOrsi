from django.shortcuts import render,redirect
from django.db import connection

# Create your views here.

def reservas (request):
    id= request.user.id
    print(id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            fecha = request.POST['date']
            hora = request.POST['hora']
            cliente = request.POST['clientes']
            reserva = 'INSERT INTO `depilacion_reservas`( `Fecha_reserva`, `Cliente_id`, `Hora_reserva`) VALUES (\'%s\',%s,\'%s\')'% (fecha,cliente,hora)
            with connection.cursor() as cursor:
                cursor.execute(reserva)
            return redirect('/')
        with connection.cursor() as cursor:
            cliente = 'select id,nombre,apellido from setup_clientes'
            cursor.execute(cliente)
            cliente = cursor.fetchall()
            clientes =[]
            for c in cliente:
                clientes.append(list(c))
            zona = 'select * from depilacion_zonas'
            cursor.execute(zona)
            zona = cursor.fetchall()
            zonas =[]
            for z in zona:
                zonas.append(list(z))
        return render(request, "Reservas/add.html",{'clientes':clientes, 'zonas':zonas})
         #otro caso redireccionamos al login
    return redirect('/login')

def reserva_list (request):
    id = request.user.id
    print(id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            fecha = request.POST['date']
            consulta = """select a.*, CONCAT(Nombre, ' ', Apellido) cliente from depilacion_reservas a inner join setup_clientes b on a.cliente_id = b.id where a.fecha_reserva = \'%s\' order by 2,4 asc""" %fecha
            print(consulta)
            with connection.cursor() as cursor:
                cursor.execute(consulta)
                consulta = cursor.fetchall()
                consulta_reserva = []
                for z in consulta:
                    consulta_reserva.append(list(z))
                return render(request, "Reservas/list.html",{'consulta': consulta_reserva})
        # otro caso redireccionamos al login
        return render(request, "Reservas/list.html")
    return redirect('/login')
