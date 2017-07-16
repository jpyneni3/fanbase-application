from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .models import Festival

def index(request):
    return render(request, 'base.html')

def signup(request):
	return render(request, 'signup.html')

def login(request):
	return render(request, 'login.html')

def festival(request):
	return render(request, 'festival.html')

def db(request):
	Festival.objects.all().delete()
	festival = Festival(begin_date = 'Saturday 17 September 2016', end_date = 'Sunday 18 September 2016', name = 'Music Midtown', artist_lineup = 'Lil Wayne, The Killers, Kesha')
	festival2 = Festival(begin_date = 'Saturday 17 September 2016', end_date = 'Sunday 18 September 2016', name = 'Music Midtown', artist_lineup = 'Lil Wayne, The Killers, Kesha')
	festival.save()
	festival2.save()
	festivals = Festival.objects.all()
	return render(request, 'db.html', {'festivals': festivals})