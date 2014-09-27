from django.contrib import admin

# Register your models here.

from models import *

@admin.register(Author)
class OfferAdmin(admin.ModelAdmin):
	pass

