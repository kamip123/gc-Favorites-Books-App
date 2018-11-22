from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AuthorForm, BookForm


def addthings(request):
	from google.cloud import storage
	storage_client = storage.Client()
	formAuthor = AuthorForm()
	formBook = BookForm()
	if request.method == 'POST':	
		if 'authorFormButton' in request.POST:
			form = AuthorForm(request.POST)
			if form.is_valid():
				author = form.save()
				return render(request, 'indexAdd.html', {'formAuthor':formAuthor, 'formBook':formBook})
			else: 
				return render(request, 'indexAdd.html', {'formAuthor':form, 'formBook':formBook})
		elif 'bookFormButton' in request.POST:		
			form = BookForm(request.POST, request.FILES)
			if form.is_valid():
				book = form.save()
				#testurl = book.bookCover.url
				testurl = book.bookCover
				return render(request, 'indexAdd.html', {'formAuthor':formAuthor, 'formBook':formBook, 'testurl':testurl})
			else: 
				return render(request, 'indexAdd.html', {'formBook':form, 'formAuthor':formAuthor})
	else: 
		return render(request, 'indexAdd.html', {'formAuthor':formAuthor, 'formBook':formBook})
	
	
	