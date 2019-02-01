# from django.contrib.auth.models import Group
from brumadinho.models import Geolocation, VisitedLocation, FoundPeople
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializer
# from django.core.serializers import serialize
from django.contrib.gis.geos import Point


class GeolocationSerializer(gis_serializer.GeoFeatureModelSerializer):

    # TODO corrigir para que coordinates NÃO SEJA exibido como valor de input na tela
    # nem seja possível de ser recebido na requisição.

    class Meta:
        model = Geolocation
        fields = ("latitude", "longitude")
        geo_field = "coordinates"
        read_only_field = "coordinates"
        write_only_fields = ("latitude", "longitude")

    def create(self, data):
        
        data['coordinates'] = Point(
            data.get('longitude'),
            data.get('latitude')
        )
        Geolocation.objects.create(**data)
        return data

class VisitedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedLocation
        fields = "__all__"

    location = GeolocationSerializer(
        read_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Geolocation.objects.all(),
        source="location",
        help_text="Geoposition ID list."
    )

    def validate_encounter_number(self, number):
        return 0 if number < 0 else number

class FoundPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundPeople
        fields = "__all__"

    location = GeolocationSerializer(
        read_only=True,
        required=False,
        allow_null=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Geolocation.objects.all(),
        help_text="Geoposition ID list.",
        source="location",
        required=False,
        allow_null=True
    )
