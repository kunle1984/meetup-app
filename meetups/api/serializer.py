from rest_framework.serializers import ModelSerializer
from meetups.models import Meetup, myUser
from rest_framework.authtoken.views import Token


class MeetupSerializer(ModelSerializer):
    class Meta:
        model = Meetup
        #fields =['id','title', 'user', 'slug']
        fields='__all__'
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = myUser
        fields=['name', 'username', 'password', 'email']
        #To make sure that the password is not displayed and to encrypt the passwod
        extra_kwargs={'password':{
            'write_only':True,
            'required':True
        }
        }
    def create(self, validated_data):
            user=myUser.objects.create_user(**validated_data)
            #creating token
            AuthToken.objects.create(user)[1]
            return user

 