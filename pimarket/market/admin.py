from django.contrib import admin

# Register your models here.

from models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	pass
	
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
	pass

@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
	pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	pass

@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
	pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	pass