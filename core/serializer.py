from rest_framework import serializers
from rooms.models import Room
from users.serializer import TinyUserSerializer

class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Room
        fields = ("pk", "price", "name", "address", "user")

class EachRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("__all__")