from rest_framework import routers
from addAuthBook.viewsets import AuthorViewSet, BookViewSet
from userProfil.viewsets import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profil', ProfileViewSet)
router.register(r'autor', AuthorViewSet)
router.register(r'ksiazka', BookViewSet)