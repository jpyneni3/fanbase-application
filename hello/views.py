from django.shortcuts import render
from django.http import HttpResponse

from .models import User
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'base.html')

def signup(request):
	return render(request, 'signup.html')

def login(request):
	return render(request, 'login.html')

def festival(request):
	return render(request, 'festival.html')

def db(request):
	User.objects.all().delete()
	user = User(username="Jas",password="password")
	user.save()
	users = User.objects.all()
	return render(request, 'db.html', {'users': users})