from django.urls import path, include
from rest_framework import routers

from .views import LocationViewSet

app_name = 'forsquare_api'

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
]

urlpatterns += router.urls
