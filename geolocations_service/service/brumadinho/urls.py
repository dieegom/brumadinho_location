from brumadinho.views import GeolocationViewSet, VisitedLocationViewSet
from rest_framework import renderers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from brumadinho import views


geolocation_list = GeolocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

visited_location_list = VisitedLocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

geolocation_detail = GeolocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

visited_location_detail = VisitedLocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('geolocations/', geolocation_list, name="geolocation-list"),
    path('visited_locations/', visited_location_list, name="visited_location-list"),
])
