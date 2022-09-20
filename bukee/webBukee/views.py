from django.shortcuts import render, HttpResponse
from productos.models import Producto
from .models import Categorias
# Create your views here.

def home(request):
    return render(request, "webBukee/base.html")

def index(request):
    return render(request, "webBukee/pages/index.html")

def contacto(request):
    return render(request, "webBukee/pages/Contacto.html")

def preguntas(request):
    return render(request, "webBukee/pages/preguntas.html")

def nosotros(request):
    return render(request, "webBukee/pages/sobreNosotros.html")

def productos(request):
    return render(request, "productos/productos.html")

def producto(request):
    tipo = Categorias.objects.all()
    producto = Producto.objects.all()
    return render(request, "webBukee/base.html", {'producto':producto, 'tipo': tipo})