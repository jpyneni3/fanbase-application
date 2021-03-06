from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db/', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', hello.views.signup, name='signup'),
    url(r'^login/', hello.views.login, name='login'),
    url(r'^festival/', hello.views.festival, name='festival'),
    url(r'^hotel/', hello.views.hotel, name='hotel'),
    url(r'^flight/', hello.views.flight, name='flight'),
    url(r'^confirmation/', hello.views.confirmation, name='confirmation'),
    url(r'^itinerary/', hello.views.itinerary, name='itinerary'),
    url(r'^test/', hello.views.test, name='test')
]
