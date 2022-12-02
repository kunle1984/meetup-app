from posixpath import basename
from django.urls import path, include
from . import views
from .views import  MeetupList, User
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('meetups', MeetupList, basename='meetups')
router.register('users', User, basename='users')
urlpatterns = [
   path('', include(router.urls))
   # path('meetups/', MeetupList.as_view()),
   # path('meetup/<int:id>', MeetupDetails.as_view()),
   
]
