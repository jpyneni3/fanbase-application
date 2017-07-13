from django.conf.urls import url,
from . import views

app_name = 'music'

urlpatterns = [
	url(r'^$', views.base, name='base'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.login, name='login')
] 