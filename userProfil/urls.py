from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_profil, name='show_profil'),
    path('favoritelist', views.favoriteBookList, name='favoriteBookList'),
    path('allbookslist', views.allBooksList, name='allBooksList'),
    path('allauthorslist', views.allAuthorList, name='allAuthorList'),
]