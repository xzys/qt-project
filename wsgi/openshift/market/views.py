from django.shortcuts import render, render_to_response
from market.models import UserProfile, Location, \
	Offer, Itemgroup. Item, Textbook, TIcket
import json
from django.core import serializers

# backend views

"""this will give you all the listings in the current view

QUERY PARAMETERS
	category


"""
@login_required
def get_json():
	# REFERENCE from market.models.Item
	# ITEM_TYPES = (
	# 	('A', 'Textbook')
	# 	('B', 'Tickets')
	# )


	# assert
	# request.method == 'GET':

	results = {}
	
	# top level category 
	category 		= request.GET.get('category', '')

	# filters that they have given
	# filters will be empty on first request
	locations 		= request.GET.get('locations', '')
	itemgroups 		= request.GET.get('itemgroups', '')


	results['filters'] = serializers.serialize('python',
		ItemGroup.objects.filter(type=category))

	# textbooks
	if category == 'A':
		results['listings'] = serializers.serialize('python',
			Textbook.objects.filter(),
			fields=(
				'condition',
				'author',
				'isbn',
				'title',
				)
			)

	# tickets
	if category == 'B':
		results['listings'] = serializers.serialize('python',
			Tickets.objects.filter(),
			fields=(
				'event',
				'date',
				)
			)

	jsondata = json.dumps({
		'filters' : results['filters'],
		'listings' : results['listings']
		})
	return HttpResponse(jsondata, content_type='application/json')

def login_req():
	pass

def logout_req():
	pass

def 





# frontend views
def home(request):
	print "HOME SWETT"
	return render_to_response("market/index.html")

def login(request):
	print "LOGIN INING"
	# return render_to_response('home/home.html')
	return render_to_response("market/login.html")