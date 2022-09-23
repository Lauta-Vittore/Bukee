from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from CarritoApp.Carrito import Carrito
from productos.models import Producto



def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)
    carrito.agregar(producto)
    return redirect("producto")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)
    carrito.eliminar(producto)
    return redirect("producto")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)
    carrito.restar(producto)
    return redirect("producto")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("producto")

def carrito(request):
    return render(request, "CarritoApp/carrito.html")