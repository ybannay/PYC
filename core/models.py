from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ActOcio(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion = models.CharField(max_length=800)	
	Imagen = models.CharField(max_length=800)
	Precio=models.CharField(max_length=800)
	Fecha=models.CharField(max_length=60)	
	Hora = models.CharField(max_length=800)	
	Aforo_Max = models.CharField(max_length=800)	
	Usuario_owner=models.CharField(max_length=200)


class ActVivienda(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion=models.CharField(max_length=800)	
	Imagen=models.CharField(max_length=800)
	Precio=models.CharField(max_length=800)
	NumHab=models.CharField(max_length=10)
	Fecha=models.CharField(max_length=60)	
	Hora = models.CharField(max_length=800)		
	TipoOferta=models.CharField(max_length=15)		
	Usuario_owner=models.CharField(max_length=200)


class ActEmpleo(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion = models.CharField(max_length=800)	
	Sueldo=models.CharField(max_length=10)
	Periodo=models.CharField(max_length=50)
	Fecha=models.CharField(max_length=60)	
	Hora = models.CharField(max_length=800)	
	Plazas = models.CharField(max_length=800)	
	Usuario_owner=models.CharField(max_length=200)


#class Usuario(models.Model):
#	User=models.CharField(max_length=100)	
#	ActSubscrita=models.CharField(max_length=300)
#	Categoria=models.CharField(max_length=15)

class Usuario(models.Model):
	title=models.CharField(_('Title'), blank=True, max_length=200)
	start=models.DateTimeField(_('Start'),null=True)
	end=models.DateTimeField(_('End'),null=True)
	all_day=models.BooleanField(_('All day'), default=False)
	url=models.CharField(max_length=100)
	User=models.CharField(max_length=100)	
	Categoria=models.CharField(max_length=15)
	
	class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')

		def __unicode__(self):
			return self.title

