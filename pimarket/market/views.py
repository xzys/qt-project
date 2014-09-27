from django.shortcuts import render

# Create your views here.

def home(request):
	print "CALLED HOME"
	print render_to_response("splash.html")