import re
from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
	class Meta:
		model=Author
		fields = ['imie','nazwisko','wiek',]
		
		
class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields = ['author', 'name','ipn','wydawnictwo','data','iloscStron', 'cena', 'bookCover',]