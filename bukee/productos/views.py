from django.shortcuts import render
from .models import Producto

# Create your views here.

def producto(request):
    producto = Producto.objects.all()
    return render(request, "productos/productos.html", {'producto':producto})