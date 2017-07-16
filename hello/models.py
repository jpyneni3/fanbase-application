from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class User(models.Model):
 	username = models.CharField(max_length = 30)
 	password = models.CharField(max_length = 30)
 	email = models.CharField(max_length = 30)

class Festival(models.Model):
	begin_date = models.CharField(max_length = 60)
	end_date = models.CharField(max_length = 60)
	name = models.CharField(max_length = 60)
	artist_lineup = models.CharField(max_length = 60)
