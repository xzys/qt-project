from django.forms import *
from django.contrib.auth.models import User

class UserForm(Form):
	username = CharField(label='Your name', max_length=100)
	password = CharField(widget=PasswordInput)

	def __init__(self, *args, **kwargs):
		super(Form, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'form-netid','placeholder':'Net ID', 'type':"text"})
		self.fields['password'].widget.attrs.update({'class':'form-password','placeholder':'Password','type':'password'})