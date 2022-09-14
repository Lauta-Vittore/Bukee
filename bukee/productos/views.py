from django.shortcuts import render
from .models import Producto
from webBukee.models import Categorias

# Create your views here.

""" def producto(request):
    productoBuzo = Producto.objects.filter(tipoproducto = 'buzo')
    productoRemera = Producto.objects.filter(tipoproducto = 'remera')
    productoCuello = Producto.objects.filter(tipoproducto = 'cuellito')

    return render(request, "productos/productos.html", {'productoBuzo':productoBuzo, 'productoRemera':productoRemera, 'productoCuello':productoCuello}) """


def producto(request):
    tipo = Categorias.objects.all()
    producto = Producto.objects.all()
    return render(request, "productos/productos.html", {'producto':producto, 'tipo': tipo})