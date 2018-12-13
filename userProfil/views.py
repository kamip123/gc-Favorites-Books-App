from django.shortcuts import render
from addAuthBook.models import Book, Author
from .models import Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from reglog.views import reg_log_main


@login_required(login_url=reg_log_main)
def show_profil(request):
	bookListt = Profile.objects.get(user=request.user)
	bookList = bookListt.favoriteBooks.all()
	
	return render(request, 'indexProfil.html', {'bookList': bookList}) 	
	