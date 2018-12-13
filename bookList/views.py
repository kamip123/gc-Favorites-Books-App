from django.shortcuts import render
from addAuthBook.models import Book
from userProfil.models import favoriteBook, Profile
from django.contrib.auth.decorators import login_required
from reglog.views import reg_log_main


@login_required(login_url=reg_log_main)
def showBooks(request):
	if request.method == 'POST':
		book = Book.objects.get(id=int(request.POST.get('bookId', False)))
		profile = Profile.objects.get(user=request.user)
		profile.favoriteBooks.add(book)
	
	bookList = Book.objects.all()
	return render(request, 'indexBookList.html', {'bookList': bookList}) 
