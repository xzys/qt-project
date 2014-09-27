from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType



class UserProfile(models.Model):
	# simple reference to django User
	user 		= models.OneToOneField(User, primary_key=True)

	# Preferences
	groups 		= models.ManyToManyField('ItemGroup',	\
		related_name = 'a+',	\
		null = True, blank = False)

	locations 	= models.ManyToManyField('Location',	\
		related_name = 'b+',	\
		null = True, blank = False)
	
	def __unicode__(self):
		return self.user.username

class Location(models.Model):
	name 		= models.CharField(max_length=100)
	lattitude 	= models.FloatField()
	longitude 	= models.FloatField() 

	def __unicode__(self):
		return str(self.longitude) + ', ' + str(self.lattitude)

class Offer(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	item = generic.GenericForeignKey('content_type', 'object_id')
	buyer        = models.ForeignKey('UserProfile', \
		related_name = 'd+')
	seller       = models.ForeignKey('UserProfile',	\
		related_name = 'e+')
	date_created = models.DateField(auto_now_add=True)
	date_sold    = models.DateField()




############### ITEMS ######################
class ItemGroup(models.Model):
	ITEM_TYPES = (
		('A', 'Textbook'),
		('B', 'Tickets'),
	)

	name 		= models.CharField(max_length=100)
	type 		= models.CharField(max_length=2, choices=ITEM_TYPES)

	def __unicode__(self):
		return self.name

# represents any item to sell
class Item(models.Model):
	seller		= models.ForeignKey(User, related_name='r+')
	price		= models.DecimalField(max_digits=6, decimal_places=2)

class Textbook(Item):
	CONDITION_CHOICES = (
		('C1', 'Poor'),
		('C2', 'Heavily Used'),
		('C3', 'Lightly Used'),
		('C4', "Its' aight"),
		('C5', 'New'),
	)

	condition 	= models.CharField(max_length=2,choices=CONDITION_CHOICES)
	author 		= models.CharField(max_length=100)
	isbn 		= models.CharField(max_length=100)
	title 		= models.CharField(max_length=100)

	def __unicode__(self):
		return "%s by %s" % (str(self.title),str(self.author))

class Ticket(Item):
	event 		= models.CharField(max_length=100)
	date 		= models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.event

