from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

#class User(models.Model):
# 	username = models.charField(max_length = 30)
# 	password = models.charField(max_length = 30)
# 	email = models.charField(max_length = 30)

# class Festval(models.Model):
# 	begin_date = models.charField(max_length = 30)
# 	end_date = models.charField(max_length = 30)
# 	name = models.charField(max_length = 30)
# 	artist_lineup = models.charField(max_length = 30)
