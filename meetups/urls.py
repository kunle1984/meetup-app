from django.urls import path

from meetups.forms import ContactForm
from . import views
from .views import MeetupUpdate, MeetupsCreate, MeetupDelete, SpeakerUpdate, SpeakerDelete,Contact
from django.contrib.auth.views import LogoutView

urlpatterns=[
path('login/', views.loginPage, name='login'),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
path('register/', views.register, name='register'),
path('profile/<str:pk>/', views.profile, name='user-profile'),
path('', views.index, name='meetups'),
path('upcoming-meetups', views.upcoming_meetups, name='upcoming-meetups'),
path('contact', Contact.as_view(), name='contact'),
path('user-meetups/<str:pk>', views.user_meetups, name='user-meetups'),
path('user-speakers/<str:pk>', views.user_speakers, name='user-speakers'),
path('create-meetups', MeetupsCreate.as_view(), name='create-meetups'),
path('meetups/success', views.confirm_registration, name='confirm-registration'),
path('contact/success', views.contact_success, name='contact-success'),
path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
path('speakers/<slug:meetup_slug>', views.add_speakers, name='add-speakers'),
path('meetup-update/<int:pk>', MeetupUpdate.as_view(), name='meetup-update'),
path('speaker-update/<int:pk>', SpeakerUpdate.as_view(), name='speaker-update'),
path('user-details/<int:pk>', views.user_details, name='user-details'),
path('participants/<int:meetupid>', views.participants, name='participants'),
path('meetup-delete/<int:pk>', MeetupDelete.as_view(), name='meetup-delete'),
path('speaker-delete/<int:pk>', SpeakerDelete.as_view(), name='speaker-delete'),


]
