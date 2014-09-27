from django.shortcuts import render, render_to_response


# Create your views here.

def home(request):
	print "CALLED HOME"
	return render_to_response("splash.html")