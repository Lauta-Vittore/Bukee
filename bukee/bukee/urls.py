"""bukee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webBukee import views
from django.conf import settings
from productos import views as productos_views
from CarritoApp.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('preguntas/', views.preguntas, name="preguntas"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos"),
    path('producto/',productos_views.producto, name="producto"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)