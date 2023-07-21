from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from GestSeguir.forms import formcontact
# Create your views here.

def home(request):
    
    return render(request, "ProyectoSegApp/home.html")

def servicios (request):
    
    return render(request, "ProyectoSegApp/servicios.html")

def cuestionario (request):

    return render(request, "ProyectoSegApp/cuestionario.html")

def blog(request):

    return render(request, "ProyectoSegApp/blog.html")

def contacto(request):
    return render(request, "ProyectoSegApp/contacto.html")

def enc_egre(request):

    return render(request, "ProyectoSegApp/enc_egre.html")

def enc_emp(request):
    return render(request, "ProyectoSegApp/enc_emp.html")