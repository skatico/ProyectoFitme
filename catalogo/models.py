from django.db import models
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


	#Create your models here.

		


    
	
    
	
		


	#status = models.CharField(
	#	max_length=1,
	#	choices=LOAN_STATUS,
	#	blank=True,
	#	default='m',
	#	help_text='Book availability',
	#)

	#class Meta:
	#	ordering = ['due_back']

	
		
class Usuario(models.Model):
	"""Model representing an author."""
	
	primer_nombre = models.CharField(max_length=100 )
	apellido = models.CharField(max_length=100)
	fecha_nac = models.DateField(null=True, blank=True)
	
	
	
	LOAN_STATUS = (
		('f','Femenino'),
		('M', 'Masculino'),
	)

	genero = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='f',
		help_text='Seleccione Genero'
	)
	

	class Meta:
		ordering = ['apellido', 'primer_nombre']

	

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'

class Entrenador(models.Model):
	"""Model representing an Entrenador."""
	
	primer_nombre = models.CharField(max_length=100 )
	apellido = models.CharField(max_length=100)
	fecha_nac = models.DateField(null=True, blank=True)
	
	
	
	LOAN_STATUS = (
		('F','Femenino'),
		('M', 'Masculino'),
	)

	genero = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='f',
		help_text='Seleccione Genero'
	)

	
	

	class Meta:
		ordering = ['apellido', 'primer_nombre']

	

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'

	
		
		
		
			
		
