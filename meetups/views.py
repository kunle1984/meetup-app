from dataclasses import field
from itertools import count
from django.shortcuts import render
from urllib import request
from string import punctuation
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Meetup, Participant, Speaker, myUser
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, RegistrationForm, MyUserRegistrationForm, ProfileForm, MeetupForm,SpeakerForm, UseMeetupForm,ContactForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
import datetime

# Create your views here.


def loginPage(request):
    page='Login'
    if request.user.is_authenticated:
        return redirect('meetups')
    #when submit botti=on is pressed 
    if request.method=='POST':  
        email = request.POST.get('email')
        email.lower()
        password = request.POST.get('password')
        try:
            user=myUser.objects.get(email=email)  
        except:
            messages.error(request, 'User does not exist')
        user=authenticate(request, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect ('meetups')
        else:
          messages.error(request, 'Username OR password does not exit')
    context={'page':page}

    return render(request, 'meetups/login.html', context)


def register(request):
    page='Register'
    form=MyUserRegistrationForm()
    context={'form':form,  'page':page}

    if request.method == 'POST':
        form = MyUserRegistrationForm(request.POST,  request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            #email=user.email
            user.save()
            #send_mail('Thanks for registering','Thanks For Registering, we will get i touch with you soon..', settings.EMAIL_HOST_USER, [ email,])
            login(request, user)
            return redirect('meetups')
        else:
            messages.error(request, 'An error occurred during registration')
           
    return render(request, 'meetups/register.html',context )


def index(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    meetups=Meetup.objects.filter(activate=True)

    todayDate=datetime.date.today()
       
    meetups=meetups.filter(
        
        Q(title__icontains=q)|
        Q(location__name__icontains=q)|
        Q(from_date__icontains=q)|
        Q(to_date__icontains=q)
        ) 
    
    count=meetups.count()
    meetups=meetups.order_by('-create')
    return render(request, 'meetups/meetups.html', {'meetups':meetups, 'todayDate':todayDate, 'count':count} )


#Upcoming Meetups
def upcoming_meetups(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    meetups=Meetup.objects.filter(activate=True)
    todayDate=datetime.date.today()
       
    meetups=meetups.filter(
        
        Q(title__icontains=q)|
        Q(location__name__icontains=q)|
        Q(from_date__icontains=q)|
        Q(to_date__icontains=q)
        ) 
    
  
    meetups=meetups.order_by('-create')
    return render(request, 'meetups/upcoming_meetups.html', {'meetups':meetups, 'todayDate':todayDate} )
#user meetups
@login_required(login_url='login')
def user_meetups(request, pk):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    
    user_meetups=Meetup.objects.order_by('-create')
    user_meetups=Meetup.objects.filter(user=pk)

    meetups=user_meetups.filter(
        Q(title__icontains=q)|
         Q(location__name__icontains=q)
        ) 
    return render(request, 'meetups/user_meetups.html', {'meetups':meetups} )

#Getting details of meetups
def meetup_details(request, meetup_slug):
   # selected_meetup=Meetup.objects.get(slug=meetup_slug)
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        speakers=selected_meetup.meetup_speakers.all
        if request.method=='GET':
            registration_form=RegistrationForm()
        else:
            registration_form= RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant=registration_form.save()
                selected_meetup.participant.add(participant)
                return redirect('confirm-registration')
                
        return render(request, 'meetups/meetup_details.html', {
         'meet_found':True,
         'meetup':selected_meetup,
         'form': registration_form ,
         'speakers':speakers, 

          })    
   
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
         'meet_found':False,
         
     })


#Add speakers to meetup
@login_required(login_url='login')
def add_speakers(request, meetup_slug):
   # selected_meetup=Meetup.objects.get(slug=meetup_slug)
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        
        if request.method=='GET':
            add_speaker_form=SpeakerForm()
        else:
           
            add_speaker_form= SpeakerForm(request.POST, request.FILES)
            if add_speaker_form.is_valid():
                add_speaker_form.instance.user=request.user
                
                speaker=add_speaker_form.save(commit=False)
                add_speaker_form.instance.meetup_name=selected_meetup.title
                speaker=add_speaker_form.save()
                selected_meetup.meetup_speakers.add(speaker)
                return redirect('meetups')
              
        return render(request, 'meetups/add_speakers.html', {
         'meet_found':True,
         'meetup':selected_meetup,
         'page':False, 
         'form': add_speaker_form ,
         

          })    
   
    except Exception as exc:
        return render(request, 'meetups/add_speakers.html', {
         'meet_found':False,
         
     })
#Show Speaker
@login_required(login_url='login')
def user_speakers(request, pk):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    
    user_speakers=Speaker.objects.order_by('-id')
    user_speakers=Speaker.objects.filter(user=pk)
    speakers=user_speakers.filter(
        Q(name__icontains=q)|
        Q(meetup_name__icontains=q)
        
        ) 
    count=user_speakers.count()
    return render(request, 'meetups/user_speakers.html', {'speakers':speakers, 'count':count} )

#speakers update
class SpeakerUpdate(LoginRequiredMixin, UpdateView):
    model=Speaker
    form_class = SpeakerForm
    template_name='meetups/add_speakers.html'
    success_url=reverse_lazy('meetups')
    
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(SpeakerUpdate, self).form_valid(form)
    
#Delete Speakers
class SpeakerDelete(LoginRequiredMixin,DeleteView):
    model=Speaker
    context_object_name='speaker'
    template_name='meetups/delete_speaker.html'
    success_url=reverse_lazy('meetups')


#add meetups class
class MeetupsCreate(LoginRequiredMixin,CreateView):
    model=Meetup
    form_class = UseMeetupForm
    #exclude=[]
    success_url=reverse_lazy('meetups')
    template_name='meetups/meetup_form.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        for i in punctuation:
            form.instance.title=form.instance.title.replace(i, ' ')
        form.instance.slug=form.instance.title.replace(' ', '-')
        return super(MeetupsCreate, self).form_valid(form)

#Delete Meetups
class MeetupDelete(LoginRequiredMixin,DeleteView):
    model=Meetup
    context_object_name='meetup'
    template_name='meetups/delete_meetup.html'
    success_url=reverse_lazy('meetups')


#Update Meetups
class MeetupUpdate(LoginRequiredMixin,UpdateView):
    model=Meetup
    form_class = UseMeetupForm
    template_name='meetups/meetup_form.html'
    success_url=reverse_lazy('meetups')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(MeetupUpdate, self).form_valid(form)
    
@login_required(login_url='login')
def profile(request, pk):
    page="Profile"
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    context={'form':form, 'page':page}
    return render(request, 'meetups/profile_form.html', context)
#contact
class Contact(FormView):
    template_name = 'meetups/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

#Meetup Participant
@login_required(login_url='login')
def participants(request, meetupid):
    meetup=Meetup.objects.get(id=meetupid)
    participants=meetup.participant.all()
    participants=participants.order_by('-id')
    count=participants.count()
    
    return render(request, 'meetups/participants.html', {'participants':participants, 'count':count} )



#User details
@login_required(login_url='login')
def user_details(request, pk):
    user=myUser.objects.get(id=pk)
    return render(request, 'meetups/user_details.html', {'user':user})
    
#Contact Success

def contact_success(request):
    return render(request, 'meetups/contact_success.html')
def confirm_registration(request):
    return render(request, 'meetups/registration_success.html')
