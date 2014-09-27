from django.shortcuts import render, render_to_response, redirect
from .forms import UserForm
from django.http import \
	HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.models import User
from market.models import \
	UserProfile, Location, Offer, ItemGroup, Item, Textbook, Ticket
import random
import json
from django.contrib.auth.models import User
from django.core import serializers
import django.contrib.auth
from django.contrib.auth.hashers import make_password
import datetime

dthandler = lambda obj: (obj.isoformat() 
                        if isinstance(obj, datetime.datetime) 
                        or isinstance(obj, datetime.date)
                        else None)
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
		
		# make the random data 
		titles = ('Math', 'Science', 'Philosophy', 'Social Sciences', 'Drinking', 'Computers')
		locations = ('North Campus', 'West Campus', 'Collegetown')
		events = ('Bill Gates', 'Icono Pop', 'Iron & Wine')

		loc = Location()
		loc.name = locations[random.choice(range(len(locations)))]
		loc.lattitude = random.random() * 10
		loc.longitude = random.random() * 10
		loc.save()
		
		tb = Textbook()
		tb.seller = User.objects.all()[0]
		tb.price = round(random.random() * 100, 2)
		tb.condition = 'C' + str(random.choice(range(5)))
		tb.isbn = str(random.random() * 10000 )
		tb.title = 'Intro to ' + titles[random.choice(range(len(titles)))]
		tb.location = loc
		tb.save()

		tx = Ticket()
		tx.seller = User.objects.all()[0]
		tx.price = round(random.random() * 100, 2)
		tx.location = loc
		tx.event = events[random.choice(range(len(events)))]
		tx.date = datetime.date.today()
		tx.save()


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
			}, default=dthandler)

        return HttpResponse(jsondata, content_type='application/json')


# login requests
def login_req(request):
	#redirect()
	pass

def logout_req(request):
	pass



# frontend views

def login(request):
	# POST request
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			if request.POST.get('Login') == 'Login':
				user = django.contrib.auth.authenticate(username=form_data['username']+"@cornell.edu",password=form_data['password'])
				if user is not None:
					django.contrib.auth.login(request,user)
					return redirect('/')
				else:
					return redirect('/login/')
			elif request.POST.get('Register') == 'Register':
				try:
					User.objects.get(email=form_data['username'])
				except Exception as e:
					new_user = User(username=form_data['username']+"@cornell.edu",password=make_password(form_data['password']))
					new_user.save()
					new_user = django.contrib.auth.authenticate(username=new_user.username,password=form_data['password'])
					django.contrib.auth.login(request,new_user)
					return redirect('/')
	elif request.method == 'GET':
		form = UserForm()
		return render(request,"market/login.html",{'form' : form})




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

	context.update(csrf(request))
	return render(request, "market/index.html", context)


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
			Ticket.objects.filter(),
			fields=(
				'event',
				'date',
				)
			)

		# SORTING HERE

	return result

