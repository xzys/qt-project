from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required

from market.models import \
	UserProfile, Location, Offer, ItemGroup, Item, Textbook, Ticket
import json
from django.core import serializers

# backend views

"""this will give you all the listings in the current view

QUERY PARAMETERS
	category e.g. A, B, C

	locations e.g. their keys
	itemgroups e.g. their keys

RETURNS
	filters
	user_groups
	user_locations
	listings



"""
# @login_required
def get_json(request, action):
	# assert
	# request.method == 'GET':
	if action == 'getjson':
		results = {}
		
		# top level category 
		category 		= request.GET.get('category', '')

		# filters that they have given
		# filters will be empty on first request
		locations 		= request.GET.get('locations', '')
		itemgroups 		= request.GET.get('itemgroups', '')
		sort 			= request.GET.get('sort', '')


		results['filters'] = serializers.serialize('python',
			ItemGroup.objects.filter(type=category))

        results['listings'] = get_listings(category)

        jsondata = json.dumps({
			'filters' : results['filters'],
			'listings' : results['listings'],
			})

        return HttpResponse(jsondata, content_type='application/json')


"""helper method to get listings"""
def get_listings(category):
	# REFERENCE from market.models.Item
	# ITEM_TYPES = (
	# 	('A', 'Textbook')
	# 	('B', 'Tickets')
	# )
	result = []
	# textbooks
	if category == 'A':
		result = serializers.serialize('python',
			Textbook.objects.filter(),
			fields=(
				'condition',
				'author',
				'isbn',
				'title',
				)
			)

		# SORTING HERE

	# tickets
	elif category == 'B':
		result = serializers.serialize('python',
			Tickets.objects.filter(),
			fields=(
				'event',
				'date',
				)
			)

		# SORTING HERE

	return result



# login requests
def login_req(request):
	pass

def logout_req(request):
	pass





"""default homepage will be textbooks"""
def default(request):
	return HttpResponseRedirect('/textbooks')


# frontend views
"""initial load
"""
def home(request, category):
	context = { 
		'subgroups' : (
				{ 'pk' : 1, 'name' : 'CS 4411'},
				{ 'pk' : 2, 'name' : 'MATH 3070'},
			 ),
		'locations': (
				{ 'pk' : 1, 'name' : 'North Campus', 'longitude' : 0.1, 'latitude' : 0.2},
				{ 'pk' : 2, 'name' : 'West Campus', 'longitude' : 0.4, 'latitude' : 0.1},
			 ),


		
		# 'filters': ItemGroup.objects.filter(type=category),
		# 'filters': ItemGroup.objects.filter(type=category),
		# 'listings' : get_listings(category),
	}

	return render(request, "market/index.html", context)



def login(request):
	context = {}
	
	return render(request, "market/login.html", context)