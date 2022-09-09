from django.contrib import admin
from .models import Categorias, Tallas
# Register your models here.

class CategoriaAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Categorias)

class TallasAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Tallas)