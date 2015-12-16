from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from oth import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/$', views.display , name='display'),
    url(r'^answer/$', views.answer , name='answer'),
    
]
