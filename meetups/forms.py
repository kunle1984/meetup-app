
from django import forms
from django.forms import CheckboxInput, ModelForm
from .models import Meetup, Participant, myUser, Speaker
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.forms import Textarea, TextInput



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields=['email']
        widgets = {
           
            'email':TextInput(
                attrs={
                    "placeholder": "Enter your email"
                }
            )
        }


class MyUserRegistrationForm(UserCreationForm):
    class Meta:
        model=myUser
        fields= ['name', 'username', 'email', 'password1', 'password2','image' ]
        widgets = {
            
            
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control"
                }
            ),
            'email':TextInput(
                attrs={
                   "placeholder": "Enter email"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter username"
                }
            ),
            'phone':TextInput(
                attrs={
                   "placeholder": "Enter phone"
                }
            )
         }



class ProfileForm(ModelForm):
    class Meta:
        model = myUser
        fields = [ 'name', 'username', 'email', 'bio', 'image', 'mobile_number', 'birth_date',]
        widgets = {
            'birth_date' : DatePickerInput(),
            'bio':Textarea(
                attrs={
                    "placeholder": "Enter your bio"
                }
            ), 
            'mobile_number':TextInput(
                
                attrs={
                    "placeholder": "Enter mobile no."
                }
            ), 
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name"
                }
            ),
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter location name"
                }
            )
           
            
        }


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields =['name', 'email','phone', 'bio', 'image']
        widgets = {
            
            'bio':Textarea(
                attrs={
                    "placeholder": "Enter bio"
                }
            ),
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name"
                }
            ),
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email"
                }
            ),
            'phone':TextInput(
                attrs={
                   "placeholder": "Enter  phone no"
                }
            )
           
        }

class MeetupForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields ='__all__'



class UseMeetupForm(forms.ModelForm):
    class Meta:
        model =Meetup
        fields=['title', 'from_date',  'to_date', 'meetup_time', 'description', 'organizer_email',  'location_name', 'location_address', 'activate','image',]
        widgets = {
            'meetup_date' : DatePickerInput(),
            'from_date' : DatePickerInput(),
            'to_date' : DatePickerInput(),
            'meetup_time':TimePickerInput(),
            'location_address':Textarea(
                attrs={
                    "placeholder": "Enter location address"
                }
            ),
            'activate':CheckboxInput(
                attrs={
                    "class": "form-check form-switch",
                     "id":"mySwitch",

                }
            ), 
            'description':Textarea(
                
                attrs={
                    "placeholder": "Enter meetup description",
                    'class':'form-control'
                }
            ), 
            'title':TextInput(
                attrs={
                   "placeholder": "Enter title"
                }
            ),
            
            'organizer_email':TextInput(
                attrs={
                   "placeholder": "Enter your email"
                }
            ),
            'location_name':TextInput(
                attrs={
                   "placeholder": "Enter location name"
                }
            )
           
        }

#Contact form
class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, 
        widget=forms.TextInput(attrs={'placeholder': '*Your Full Name..'}))
    phone = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': '*Your Phone No...', }))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'placeholder': '*Your email..'}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'placeholder': '*Your subject..'}))
   
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '*Your Message..'}))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )