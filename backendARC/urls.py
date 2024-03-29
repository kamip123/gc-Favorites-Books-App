"""backendARC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .routers import router
from django.views.generic import TemplateView

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dodaj/', include('addAuthBook.urls')),
    path('profil/', include('userProfil.urls')),
    path('bookList/', include('bookList.urls')),
    path('api/', include(router.urls)),
    path('', include('reglog.urls')),
    path('weather/', include('weather.urls')),
    path('scheduleTasks/', include('scheduleTasks.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #tutaj dodaj adresy ktore chcesz np:
    #path('adres/', TemplateView.as_view(template_name='jakasnazwa.html')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
