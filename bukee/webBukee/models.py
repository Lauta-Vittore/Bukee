from django.db import models

# Create your models here.
class Categorias(models.Model):
    tipocategoria = models.CharField(db_column='tipoCategoria', primary_key=True, blank=True,  max_length = 30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categorias'

    def __str__(self):
        return self.tipocategoria


class Tallas(models.Model):
    talla = models.CharField(db_column='Talla', primary_key=True, blank=True, max_length = 30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tallas'

    def __str__(self):
        return self.talla