from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
def findFlights(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def saveReservation(request):
    flight=Flight.objects.get(id=request.data['id'])
    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.email=request.data['email']
    passenger.phoneNumber=request.data['phoneNumber']
    passenger.save()
    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger
    reservation.save()
    return Response("Reservation saved", status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


def display(request):
    return HttpResponse("Hello, World!")

