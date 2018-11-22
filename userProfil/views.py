from django.shortcuts import render
from addAuthBook.models import Book, Author
from .models import Profile
from django.http import JsonResponse

# Create your views here.
def show_profil(request):
	bookListt = Profile.objects.get(user=request.user)
	bookList = bookListt.favoriteBooks.all()
	
	return render(request, 'indexProfil.html', {'bookList': bookList}) 
	
	
def favoriteBookList(request):
	bookListt = Profile.objects.get(user=request.user) #after commenting this line it work
	bookList = bookListt.favoriteBooks.all().values()
	data = list(bookList)
	return JsonResponse(data, safe=False)	
	
def allBooksList(request):
	data = Book.objects.all().values()
	data = list(data)
	return JsonResponse(data, safe=False)	
	
def allAuthorList(request):
	if request.method == 'POST':	
		form = Author.objects.create(imie=request.POST.get('imie', False),nazwisko=request.POST.get('nazwisko', False),wiek=request.POST.get('wiek', False))
		form.save()
		
	data = Author.objects.all().values()
	data = list(data)
	return JsonResponse(data, safe=False)		
	