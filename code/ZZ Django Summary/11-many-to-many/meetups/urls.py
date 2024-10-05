from django.urls import path

from . import views

urlpatterns = [
  path('meetups/', views.index, name='all-meetups'), # our-domain.com/meetups
  path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]