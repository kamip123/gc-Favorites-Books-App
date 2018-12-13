from django.shortcuts import render
from django.core.mail import EmailMessage 
from django.contrib.auth.models import User
from django.http import HttpResponse


def send_ad_emails(request):
	users = User.objects.all()
	for user in users:
		mail_subject = 'Check this out :D'
		message = 'Test dziala ?'
		to_email = user.email
		email = EmailMessage(mail_subject, message, to=[to_email])
		email.send()
	return HttpResponse('Ads have been send.')