from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	# simple reference to django User
	user = models.OneToOneField(User, primary_key=true)

	# Preferences
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
	latitude = models.FloatField()
	longitude = models.FloatField() 

	def __unicode__(self):
		return str(self.longitude) + ', ' + str(self.lattitude)

class Offer(models.Model):
	item         = models.ForeignKey('Item')
	buyer        = models.ForeignKey('UserProfile')
	seller       = models.ForeignKey('UserProfile')
	date_created = models.DateField(auto_now_add=True)
	date_sold    = models.DateField()

############### ITEMS ######################
class ItemGroup(model.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

# represents any item to sell
class Item(models.Model):
	seller = models.ForeignKey(User, related_name='r+')
	# price is deciman 2 units
	price = models.DecimalField(max_digits=6, decimal_places=2)

	class Meta:
		abstract = True

class Textbook(Item):
	author = models.CharField(max_length=100)
	ISBN = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title, 'by:', self.author

class Ticket(Item):
	event = models.CharField(max_length=100)
	date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.event

