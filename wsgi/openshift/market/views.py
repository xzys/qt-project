from django.shortcuts import render, render_to_response, redirect
from .forms import UserForm
from django.http import \
	HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.core import serializers
from django.contrib.auth.models import User
from market.models import \
	UserProfile, Location, Offer, ItemGroup, Item, Textbook, Ticket
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth.hashers import make_password
import datetime
from  django.contrib.sessions.models import Session
import random, json, datetime, re
import django.contrib.auth
from django.contrib import messages

dthandler = lambda obj: (obj.isoformat() 
						if isinstance(obj, datetime.datetime) 
						or isinstance(obj, datetime.date)
						else None)
# backend views

@login_required
def api_request(request, action):
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
	# assert
	# request.method == 'GET':
	if action == 'getjson':
		
		# make the random data for now
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
		location_ids	= [int(s.strip()) for s in request.GET.get('locations', '').split(',') if s is not '']
		itemgroup_ids	= [int(s.strip()) for s in request.GET.get('itemgroups', '').split(',') if s is not '']
		sort_by			= request.GET.get('sort', '')


		locations 		= Location.objects.in_bulk(location_ids)
		itemgroups 		= ItemGroup.objects.in_bulk(itemgroup_ids)

		# save these locations and subgroups into user
		# to save preferences
		if len(locations) > 0:
			request.user.userprofile.locations = locations
		if len(itemgroups) > 0:
			request.user.userprofile.groups = itemgroups




		results['filters'] = serializers.serialize('python',
			ItemGroup.objects.filter(type=category))

		results['listings'] = get_listings(category)
		
		results['user_locations'] = request.user.userprofile.locations

		results['user_itemgroups'] = request.user.userprofile.groups
		
		jsondata = json.dumps({
			'filters' : results['filters'],
			'listings' : results['listings'],
			'user_locations' : results['user_locations'],
			'user_itemgroups' : results['user_itemgroups'],
			}, default=dthandler)

		return HttpResponse(jsondata, content_type='application/json')

	elif action == 'postlisting':
		"""this wll add a post to the thing

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

		# top level category 

		category = request.GET.get('category', '')
		subgroup_pk = request.GET.get('subgroup', '')
		location_pk = int(request.GET.get('location', ''))
		price = request.GET.get('price', '')

		# postdata 		= json.loads(request.body)
		# category 		= postdata['category']
		# # subgroup_pk 	= postdata['subgroup']
		# location_pk 	= postdata['location']
		# price 			= postdata['price']

		try:
			loc = Location.objects.filter(pk = location)
		except:
			loc = Location.objects.all()[0]
		pass


		if category == 'A':
			author = request.GET.get('author', '')
			isbn = request.GET.get('isbn', '')
			title = request.GET.get('title', '')
			condition = int(request.GET.get('condition', ''))

			# author		= postdata['author']
			# isbn		= int(postdata['isbn'])
			# title		= postdata['title']
			# condition	= int(postdata['condition'])


			tb = Textbook()
			tb.seller = request.user
			tb.price = float(price)
			tb.condition = 'C' + str(condition)
			tb.isbn = isbn
			
			tb.title = title
			tb.location = loc
			tb.save()

		elif category == 'B':
			event = postdata['event']
			event_date = datetime.datetime(*map(request.GET.get('event_date', ''), \
				re.split('[^\d]', s)[:-1]))
			
			# make sure you get the date like this in your js app
			# var date = new Date();
			# date.toISOString();

			tx = Ticket()
			tx.seller = request.user
			tx.price = price
			tx.location = loc
			tx.event = ItemGroup.objects.filter(pk=subgroup_pk)[0].name
			tx.date = event_date
			tx.save()

		return HttpResponse('cool dude')

	
	elif action == 'lookupisbn':
		pass
	elif action == 'search':
		query = request.GET.get('q', '')
		category = request.GET.get('category', '')

		textbook_count = 0
		ticket_count = 0

		textbooks = []
		tickets = []
		for tb in Textbook.objects.all():
			if (len(re.findall(query, tb.title, re.IGNORECASE)) > 0 or 
				len(re.findall(query, tb.author, re.IGNORECASE)) > 0 or
				len(re.findall(query, str(tb.isbn), re.IGNORECASE)) > 0):
				textbooks.append(tb)
		
		for tx in Ticket.objects.all():
			if (len(re.findall(query, tx.event, re.IGNORECASE)) > 0):
				tickets.append(tx)
				

		results = {}

		if category =='A':
			results['listings'] = serializers.serialize('python',
				textbooks,
				fields=(
					'condition',
					'author',
					'isbn',
					'title',
					)
				)

			results['other'] = '%i results in Tickets...' % len(tickets)

			
		if category =='B':
			results['listings'] = serializers.serialize('python',
				tickets,
				fields=(
					'condition',
					'author',
					'isbn',
					'title',
					)
				)

			results['other'] = '%i results in Textbooks...' % len(textbooks)

		
		
		jsondata = json.dumps({
			'listings' : results['listings'],
			'others' : results['other'],
			})
		return HttpResponse(jsondata, content_type='application/json')








def request_log_out(request):
	django.contrib.auth.logout(request)
	print "ADDING MESSAGES"
	messages.add_message(request,messages.SUCCESS,"Log Out Successful")
	return redirect("/login/")


# frontend views

def login(request):
	# POST request
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			if request.POST.get('Login') == 'Login':
				user = django.contrib.auth.authenticate(username=form_data['username']+"@cornell.edu",password=form_data['password'])
				if user is not None: # successful log in
					django.contrib.auth.login(request,user)
					return redirect('/')
				else: # Either username or password incorrect
					messages.add_message(request,messages.ERROR,'Incorrect username or password')
					return redirect('/login/')

			elif request.POST.get('Register') == 'Register':
				try: # USER EXISTS
					User.objects.get(username=form_data['username']+"@cornell.edu")
					messages.add_message(request,messages.ERROR,'Username already exists, please log in')
					return redirect('/login/')
				except Exception as e:
					new_user = User(username=form_data['username']+"@cornell.edu",password=make_password(form_data['password']))
					new_user.save()
					new_user = django.contrib.auth.authenticate(username=new_user.username,password=form_data['password'])
					django.contrib.auth.login(request,new_user)

					new_userp = UserProfile()
					new_userp.user = new_user
					new_userp.save()
					
					return redirect('/')
	elif request.method == 'GET':
		form = UserForm()
		return render(request,"market/login.html",{'form' : form})




# frontend views
"""default homepage will be textbooks"""
def default(request):
	return HttpResponseRedirect('/textbooks')


"""post listing 
"""
def post(request):
	print "POST GENKI"
	return render(request, "market/post.html")


"""initial load
"""
def home(request, category):

	session = Session.objects.get(session_key=request.session.session_key)
	uid = session.get_decoded().get('_auth_user_id')
	user = User.objects.get(pk=uid)

	context = { 
		'subgroups' : (
				{ 'pk' : 1, 'name' : 'CS 4411'},
				{ 'pk' : 2, 'name' : 'MATH 3070'},
			 ),
		'locations': (
				{ 'pk' : 1, 'name' : 'North Campus', 'longitude' : 0.1, 'latitude' : 0.2},
				{ 'pk' : 2, 'name' : 'West Campus', 'longitude' : 0.4, 'latitude' : 0.1},
			 ), 
		'netid':user.username,
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

