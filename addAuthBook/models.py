from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
	imie = models.CharField(max_length=50)
	nazwisko = models.CharField(max_length=100)
	wiek = models.CharField(max_length=200)
	def __str__(self):
		return self.imie
	
	
class Book(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ipn = models.IntegerField()
	wydawnictwo = models.CharField(max_length=100)
	data = models.DateTimeField(default=timezone.now)
	iloscStron = models.IntegerField()
	cena = models.FloatField(max_length=10)
	bookCover = models.FileField(null=True, blank=True)
	
	def __str__(self):
		return self.name
		
	
    