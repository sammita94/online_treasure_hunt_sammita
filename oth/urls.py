from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from oth import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/$', views.display , name='display'),
    url(r'^answer/$', views.answer , name='answer'),
    url(r'^lboard/$', views.lboard , name='lboard'),
    url(r'^rules/$', views.rules , name='rules'),
    url(r'^notif/$', views.getNotif, name='getNotif'),
    # url(r'^correct/$', views.correct, name='correct'),

]
