from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Building, Room


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ['url', 'code', 'name']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'code', 'building', 'floor', 'capacity']
