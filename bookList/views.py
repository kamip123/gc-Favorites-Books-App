from django.shortcuts import render
from addAuthBook.models import Book
from userProfil.models import favoriteBook, Profile

# Create your views here.

def showBooks(request):
	if request.method == 'POST':
		book = Book.objects.get(id=int(request.POST.get('bookId', False)))
		profile = Profile.objects.get(user=request.user)
		profile.favoriteBooks.add(book)
	
	bookList = Book.objects.all()
	return render(request, 'indexBookList.html', {'bookList': bookList}) 
