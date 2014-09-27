from django.shortcuts import render, render_to_response
import json
from django.core import serializers

# backend views

"""this will give you all the listings in the current view"""
def get_json():
	results = {}

	results['listings'] = serializers.serialize('python',
		Items.objects.filter(),
		fields=(
			
			)
		)
	pass

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