from http.client import HTTPResponse
from meetups.models import Meetup, myUser

from rest_framework.decorators import api_view, APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializer import MeetupSerializer, UserSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




#using ModelView set
class MeetupList(viewsets.ModelViewSet):
    queryset=Meetup.objects.all()
    serializer_class=MeetupSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    


class User(viewsets.ModelViewSet):
    queryset=myUser.objects.all()
    serializer_class=UserSerializer




#function base api
"""@api_view(['GET', 'POST'])
def meetup_list(request):
    meetups = Meetup.objects.all()
    if request.method=="GET":
        serializer = MeetupSerializer(meetups, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = MeetupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

@api_view(['GET','PUT', 'DELETE'])
def meetup(request, pk):
    try:
        meetup = Meetup.objects.get(id=pk)
    except Meetup.DoesNotExist:
            return HTTPResponse(status=404)
        
    if request.method=='GET':

        serializer = MeetupSerializer(meetup)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer = MeetupSerializer(meetup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=401)
    elif request.method=='DELETE':
        meetup.delete()
        return HTTPResponse(status=201)"""

#class based serializer
"""
class MeetupList(APIView):
    def get(self, request):
        meetups=Meetup.objects.all()
        serializer = MeetupSerializer(meetups, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=MeetupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class MeetupDetails(APIView):

    def get_object(self, id):
        try:
            return Meetup.objects.get(id=id)
        except Meetup.DoesNotExist:
            return HTTPResponse(status=404)
    def get(self, request, id):
        meetup=self.get_object(id)
        serializer=MeetupSerializer(meetup)
        return Response(serializer.data)
    def put(self, request, id):
       meetup=self.get_object(id)
       serializer=MeetupSerializer(meetup, data=request.data)
       if serializer.is_valid():
        serializer.save()
       return Response(serializer.errors, status=400)
    def delete(self, request, id):
         meetup=self.get_object(id)
         meetup.delete()

"""
"""
class MeetupList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset=Meetup.objects.all()
    serializer_class=MeetupSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        self.create(request)
        return HTTPResponse(status=201)

class MeetupDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset=Meetup.objects.all()
    local_field='id'
    serializer_class=MeetupSerializer
    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)

"""

