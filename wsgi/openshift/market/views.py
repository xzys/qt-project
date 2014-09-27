from django.shortcuts import render, render_to_response


# Create your views here.

def home(request):
<<<<<<< HEAD
	print "HOME SWETT"
	return render_to_response("market/login.html")

def login(request):
	print "LOGIN INING"
=======
	# print "HOME SWETT HOME"
	return render_to_response("market/index.html")

def login(request):
	# print "LOGIN INING"
>>>>>>> e0e7b172d3e2d08fa7ef476f4f5b0fec936106f3
	# return render_to_response('home/home.html')
	return render_to_response("market/login.html")