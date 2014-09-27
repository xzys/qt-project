
from django.shortcuts import render, render_to_response, redirect
from .forms import UserForm
from django.http import \
	HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from market.models import \
	UserProfile, Location, Offer, ItemGroup, Item, Textbook, Ticket
import json
from django.contrib.auth.models import User
from django.core import serializers
import django.contrib.auth
from django.contrib.auth.hashers import make_password

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
	#redirect()
	pass

def logout_req(request):
	pass


# frontend views
def home(request):
	print "CALLED HOME"
	return render_to_response("market/index.html")

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
