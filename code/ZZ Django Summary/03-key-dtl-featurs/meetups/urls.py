from django.urls import path

from . import views

urlpatterns = [
  path('meetups', views.index) # our-domain.com/meetups
]