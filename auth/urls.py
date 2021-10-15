from django.urls import path
from django.urls.resolvers import URLPattern

from auth import views

urlpatterns=[
    path('login/',views.login)

]
