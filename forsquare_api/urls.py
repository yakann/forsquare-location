from django.urls import path, include

from .views import LocationViewSet

location_access_methods = {
    'get': 'list',
    'post': 'create'
}

urlpatterns = [
    path('locations/', LocationViewSet.as_view(location_access_methods), name='locations'),
]