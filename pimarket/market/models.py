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
	item         = models.CharField(max_length=30)
	buyer        = models.CharField(max_length=30)
	seller       = models.CharField(max_length=30)
	date_created = models.CharField(max_length=30)
	date_sold    =  models.CharField(max_length=30)

