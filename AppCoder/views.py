# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import Template, Context
from django.template import loader

from AppCoder.models import Persona

# Create your views here.


def menu_inicio(request) -> HttpResponse:
    return HttpResponse("Hola Mundo!!")


def mostrar_familiares(request: str) -> HttpResponse:
    template = loader.get_template("template1.html")

    familiar1 = Persona(id=1, nombre="Alejandro Magno", edad=25, fecha="2301-04-11")
    familiar2 = Persona(id=2, nombre="Julio Cesar", edad=32, fecha="1234-08-23")
    familiar3 = Persona(id=3, nombre="Neron", edad=28, fecha="1198-10-22")
    familiar1.save()
    familiar2.save()
    familiar3.save()

    diccionario = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3,
    }
    res = template.render(diccionario)

    return HttpResponse(res)
