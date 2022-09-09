from django.db import models
from webBukee.models import Categorias, Tallas
# Create your models here.

class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True, blank=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length = 30)  # Field name made lowercase.
    descripcionproducto = models.CharField(db_column='descripcionProducto', max_length = 30)  # Field name made lowercase.
    talla1 = models.ForeignKey(Tallas, models.DO_NOTHING, db_column='talla1', blank=True, related_name='talla1')
    talla2 = models.ForeignKey(Tallas, models.DO_NOTHING, db_column='talla2', blank=True, related_name='talla2')
    talla3 = models.ForeignKey(Tallas, models.DO_NOTHING, db_column='talla3', blank=True, related_name='talla3')
    talla4 = models.ForeignKey(Tallas, models.DO_NOTHING, db_column='talla4', blank=True, related_name='talla4')
    tipoproducto = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='tipoProducto', blank=True, null=True)  # Field name made lowercase.     
    precioproducto = models.TextField(db_column='precioProducto')  # Field name made lowercase. This field type is a guess.
    imagenproducto = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)  # Field name made lowercase. This field type is a guess. 

    class Meta:
        managed = False
        db_table = 'Producto'
        verbose_name= 'Productos'

    def __str__(self):
        return self.nombreproducto


