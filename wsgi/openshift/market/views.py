from django.shortcuts import render, render_to_response, redirect
from .forms import UserForm
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

def login_req(request):
	redirect()

def logout_req():
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
			form.save()
		return redirect('/')
	# GET Request
	else:
		form = UserForm()
		return render(request,"market/login.html",{'form' : form})