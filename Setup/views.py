from django.contrib.auth import authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.db import connection
# Create your views here.

# Create your views here.


import json

def welcome(request):
    # Si estamos identificados devolvemos la portada
    id= request.user.id
    print(id)
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
           # clientes= 'select count(*) from lab_clientes'
           # cursor.execute(clientes)
           # clientes= cursor.fetchone()
           # presupuestos ='select count(*) from  lab_presupuestos where fecha >= (NOW()-INTERVAL 30 DAY)'
           # cursor.execute(presupuestos)
           # presupuestos= cursor.fetchone()
           # reparaciones = 'SELECT a.id,Marca,modelo,DATE_FORMAT(Fecha_ingreso,"%Y-%m-%d")Fecha_ingreso,ifnull(evento,"Ingresado") FROM lab_reparaciones a left join lab_eventos b on a.evento_id = b.id LIMIT 15'
           # cursor.execute(reparaciones)
           # reparaciones= cursor.fetchall()
           # rep = []
           # for r in reparaciones:
           #     rep.append(list(r))
            return render(request, "home.html", )#{'clientes':clientes[0],'presupuestos':presupuestos[0],'reparaciones':rep}
         #otro caso redireccionamos al login
    return redirect('/login')


import requests

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    #ip = get_client_ip(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    # URL de la API
    api_url = "http://ip-api.com/json/"
    # Definimos los parametros de respuesta que queremos obtener
    parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
    data = {"fields": parametros}

    # Nos conectamos con la API
    res = requests.get(api_url + ip, data=data)
        # Obtenemos y procesamos la respuesta JSON
    api_json_res = json.loads(res.content)
    print (api_json_res)
    status = api_json_res['status']
    #country = api_json_res['country']
    print (status)
    #print(country)




    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')