from rest_framework.views import APIView
from rest_framework.response import Response
from rooms.models import Room
from .serializer import RoomSerializer

class ListRoomView(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)