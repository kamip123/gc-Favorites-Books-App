from django.db import models
from django.contrib.auth.models import User
from addAuthBook.models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_author = models.IntegerField(default=0)
	#favorite = models.ManyToManyField('favoriteBook')
	favoriteBooks = models.ManyToManyField('addAuthBook.Book',null=True, blank=True)
	def __str__(self):
		return str(self.is_author)

		
		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class favoriteBook(models.Model):
	bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
	how_much_favorite = models.IntegerField(default=0)
	def __str__(self):
		return str(self.how_much_favorite)
