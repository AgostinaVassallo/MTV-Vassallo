from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def familiares(request):
    fam1=Familiares(nombre="Agostina Vassallo", grado_parentesco=1,fecha_nacimiento="1990")
    fam1.save()
    cadena=f"Familiares: Nombre{fam1.nombre}, Grado parentesco: {fam1.grado_parentesco}, Fecha nacimiento: {fam1.fecha_nacimiento}"
    diccionario= {'nombre' :'Agostina Vassallo', 'grado_parentesco' :1, 'fecha_nacimiento':'1990' }

    archivo=open("C:/Users/pya/Desktop/entorno virtual/agos/Proyecto1/Plantillas/template1.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    diccionario=template.render(contexto)#llena mis espacios en blanco con los datos de mi contexto
    return HttpResponse(diccionario)

def familiares2(request):
    fam2=Familiares(nombre="Alberto Vassallo", grado_parentesco=2,fecha_nacimiento="1957")
    fam2.save()
    cadena2=f"Familiares: Nombre{fam2.nombre}, Grado parentesco: {fam2.grado_parentesco}, Fecha nacimiento: {fam2.fecha_nacimiento}"
    diccionario2= {'nombre' :'Alberto Vassallo', 'grado_parentesco' :2, 'fecha_nacimiento':'1957' }

    archivo=open("C:/Users/pya/Desktop/entorno virtual/agos/Proyecto1/Plantillas/template1.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario2)

    diccionario2=template.render(contexto)#llena mis espacios en blanco con los datos de mi contexto
    return HttpResponse(diccionario2)

def familiares3(request):
    fam3=Familiares(nombre="Pablo Vassallo", grado_parentesco=3,fecha_nacimiento="1934")
    fam3.save()
    cadena3=f"Familiares: Nombre{fam3.nombre}, Grado parentesco: {fam3.grado_parentesco}, Fecha nacimiento: {fam3.fecha_nacimiento}"
    diccionario3= {'nombre' :'Pablo Vassallo', 'grado_parentesco' :3, 'fecha_nacimiento':'1934' }

    archivo=open("C:/Users/pya/Desktop/entorno virtual/agos/Proyecto1/Plantillas/template1.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario3)

    diccionario3=template.render(contexto)#llena mis espacios en blanco con los datos de mi contexto
    return HttpResponse(diccionario3)