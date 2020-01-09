from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rooms.models import Room
from .serializer import RoomSerializer, EachRoomSerializer

class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = EachRoomSerializer