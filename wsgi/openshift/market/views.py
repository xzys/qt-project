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


"""
# @login_required
def get_json(request, action):
	# REFERENCE from market.models.Item
	# ITEM_TYPES = (
	# 	('A', 'Textbook')
	# 	('B', 'Tickets')
	# )


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
		elif category == 'B':
			results['listings'] = serializers.serialize('python',
				Tickets.objects.filter(),
				fields=(
					'event',
					'date',
					)
				)
		else:
			results['listings'] = []

		jsondata = json.dumps({
			'filters' : results['filters'],
			'listings' : results['listings'],
			})
		return HttpResponse(jsondata, content_type='application/json')

def login_req(request):
	pass

def logout_req(request):
	pass






# frontend views
def home(request):
	print "HOME SWETT"
	return render_to_response("market/index.html")

def login(request):
	print "LOGIN INING"
	# return render_to_response('home/home.html')
	return render_to_response("market/login.html")