from django.db import models
from datetime import datetime   
from django.utils import timezone
from django_countries.fields import CountryField
# Create your models here.
def end():
   return timezone.now() + timezone.timedelta(days=7)

def init():
   return timezone.now()
# este modelo es necesario para hacer una busqueda sencilla
# en la vista de los eventos por pais
# si no existiese se tendria que pasar el array de todos los paises
# al front y la dvd que flojera, mejor filtrar por los paises que tengan un evento
class Country(models.Model):
	name=CountryField(unique=True) 
	def __str__(self):
		return self.name.name

class Event(models.Model):
	title = models.CharField(max_length=149, unique=True)
	description = models.TextField(blank=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	start_date = models.DateField(default=init)
	end_date = models.DateField(default=end)
	banner_1 = models.FileField(upload_to='banners/', blank=True, null=True, default="banners/default.jpeg")
	use_banner_1 = models.BooleanField(default=False)
	banner_2 = models.FileField(upload_to='banners/', blank=True, null=True)
	use_banner_2 = models.BooleanField(default=False)
	link_1 = models.URLField(default="",null=True, blank=True) 
	link_1_text = models.CharField(max_length=300,blank=True,null=True)
	use_link_1 = models.BooleanField(default=False)
	link_2 = models.URLField(default="",null=True, blank=True) 
	link_2_text = models.CharField(max_length=300,blank=True,null=True)
	use_link_2 = models.BooleanField(default=False)

	def __str__(self):
		return self.title