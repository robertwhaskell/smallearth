from django.conf.urls import include, url, patterns
from django.contrib import admin
import views

urlpatterns = patterns('',
                       url(r'^$', views.graph_test, name='graph_test')
                       )
