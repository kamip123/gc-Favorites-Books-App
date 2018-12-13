from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('emailAd/', views.send_ad_emails, name='send_ad_emails'),
]