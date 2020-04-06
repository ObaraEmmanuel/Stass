from rest_framework import routers
from .views import RoomViewSet, BuildingViewSet

router = routers.DefaultRouter()

router.register(r'rooms', RoomViewSet)
router.register(r'buildings', BuildingViewSet)