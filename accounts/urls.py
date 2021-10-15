from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.registeruser,name='register'),
    path('login/',views.loginuser,name='login'),
    path('home/',views.home,name='home'),
    path('contect/',views.contect,name='contect'),
    path('idealweight',views.IdealWeight),
    path('testform',views.newtable),


]
