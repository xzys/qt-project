from django.db import models

# Create your models here.

class Offer(models.Model):
	item         = models.CharField(max_length=30)
	buyer        = models.CharField(max_length=30)
	seller       = models.CharField(max_length=30)
	date_created = models.CharField(max_length=30)
	date_sold    =  models.CharField(max_length=30)