from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	# reference to django User
	user = models.OneToOneField(User, primary_key=true)

	# 
	groups = models.ManyToManyField('ItemGroup',
		related_name = 'a+',
		null = True, blank = False)

	locations = models.ManyToManyField('Location',
		related_name = 'b+')
		null = True, blank = False)
	
	def __unicode__(self):
		return self.user.username



class Location(model.Model):
	name = models.CharField(max_length=100)
	# one or the other
	lattitude = models.FloatField()
	longitude = models.FloatField() 

	def __unicode__(self):
		return self.user.username

############### ITEMS ######################
class ItemGroup(model.Model):
	name = models.CharField(max_length=100)

# represents any item to sell
class Item(models.Model):
	user1 = models.ForeignKey(User, related_name='r+')
	# price is deciman 2 units
	price = models.DecimalField(max_digits=6, decimal_places=2)

	class Meta:
		abstract = True


class Textbook(Item):
	author = models.CharField(max_length=100)
	ISBN = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	title = models.CharField(max_length=100)

class Ticket(Item):
	event = models.CharField(max_length=100)
	date = models.DateTimeField(null=True, blank=True)

class Offer(models.Model):
	item         = models.ForeignKey('Item')
	buyer        = models.ForeignKey('UserProfile')
	seller       = models.ForeignKey('UserProfile')
	date_created = models.DateField(auto_now_add=True)
	date_sold    =  models.DateField()

