from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rooms.models import Room
from users.models import User
from .serializer import RoomSerializer, EachRoomSerializer
from users.serializer import UserSerializer, TinyUserSerializer

class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = EachRoomSerializer

class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = TinyUserSerializer
    
class SeeUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer