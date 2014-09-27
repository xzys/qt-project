from django.shortcuts import render, render_to_response


# Create your views here.

def home(request):
	print "HOME SWETT"
	return render_to_response("market/login.html")

def login(request):
	print "LOGIN INING"
	# return render_to_response('home/home.html')
	return render_to_response("market/login.html")