from meetups.models import Meetup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MeetupSerializer
from rest_framework import status

from meetups.api import serializer



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/meetups',
        'GET /api/meetups/:id',
        'POST /api/meetup/create',
        'POST /api/meetup/delete',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getMeetups(request):
    meetups = Meetup.objects.all()
    serializer = MeetupSerializer(meetups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMeetup(request, pk):
    meetup = Meetup.objects.get(id=pk)
    serializer = MeetupSerializer(meetup, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postMeetup(request):
    
    serializer = MeetupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
    return Response(serializer.data, status=201)

@api_view(['DELETE'])
def deleteMeetup(request, pk):
    meetup = Meetup.objects.get(id=pk)
    meetup.delete()