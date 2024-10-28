from django.shortcuts import render
from . import forms
from equipoBasket.forms import formularioEquipo
from equipoBasket.models import Equipo
# Create your views here.

def index(request):
    return render (request,'equipoBasket/index.html')

def listadoEquipos(request):
    equipos = Equipo.objects.all()
    data = {'equipos': equipos}
    return render (request,'equipoBasket/equipos.html',data)

def agregarEquipo(request):
    form = formularioEquipo()
    if request.method =='POST':
        form = formularioEquipo(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form':form}
    return render (request,'equipoBasket/agregarEquipo.html',data)