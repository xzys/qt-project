from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	# reference to django User

	user = models.OneToOneField(User, primary_key=true)


# represents any item to sell
class Item(models.Model):
	user1 = models.ForeignKey(User, related_name='r+')
	user2 = models.ForeignKey(User, related_name='b+')

	started_date = models.DateTImeField()


	class Meta:
		abstract = True

class Offer(models.Model):
	item         = models.ForeignKey('Item')
	buyer        = models.ForeignKey('UserProfile')
	seller       = models.ForeignKey('UserProfile')
	date_created = models.DateField(auto_now_add=True)
	date_sold    =  models.DateField()

