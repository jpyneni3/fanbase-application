from django.conf.urls import url,
from . import views

app_name = 'music'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.login, name='login'),
	url(r'^festival/$', views.festival, name='festival'),
	url(r'^db/$', views.db, name='db'),
	url(r'^hotel/$', views.hotel, name='hotel'),
	url(r'^flight/', hello.views.flight, name='flight')
] 