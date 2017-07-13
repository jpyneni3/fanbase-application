from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def base(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'home/base.html')

def signup(request):
	return render(request, 'home/signup.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

