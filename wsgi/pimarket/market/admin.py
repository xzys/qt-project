from django.contrib import admin
from market.models import UserProfile, Location, Offer, ItemGroup, Item, Textbook, Ticket

# Register your models here.



# @admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	pass

# @admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	pass
	
# @admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
	pass

# @admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
	pass

# @admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
	pass

# @admin.register()
class TicketAdmin(admin.ModelAdmin):
	pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Ticket, TicketAdmin)