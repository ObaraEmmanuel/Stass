from rest_framework import viewsets, permissions
from .models import Room, Building
from .serializers import RoomSerializer, BuildingSerializer
from django.http import Http404


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        code = self.request.GET.get("building")
        if code is None:
            return Room.objects.all()
        building = Building.objects.filter(code=code)
        if building.exists():
            return Room.objects.filter(building=building[0])
        raise Http404(f"Building {code} does not exist")


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = (permissions.IsAuthenticated,)
