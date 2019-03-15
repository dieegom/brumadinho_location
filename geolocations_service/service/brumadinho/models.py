from django.db import models
from django.contrib.gis.db import models as gis_models

class Geolocation(models.Model):

    coordinates = gis_models.PointField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class VisitedLocation(models.Model):

    reference = models.CharField(
        max_length=100,
        help_text="Reference and information."
    )
    location = models.ForeignKey(
        Geolocation,
        on_delete=models.PROTECT,
        help_text="Geoposition of the visited area."
    )
    visitation_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Datetime of the location analysis."
    )
    encounter_number = models.IntegerField(
        help_text="Number of people found in this location."
    )
    radius = models.FloatField(
        help_text="Radial área range of search.",
        default=1
    )
    observations = models.CharField(
        max_length=2000,
        help_text="Observations",
        blank=True,
        null=True
    )


class FoundPeople(models.Model):

    # Gender options
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    # Condition options
    ALIVE = "Alive"
    DEAD = "Dead"
    CONDITION_CHOICES = (
        (ALIVE, ALIVE),
        (DEAD, DEAD)
    )

    full_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Full name of the found people."
    )
    location = models.ForeignKey(
        Geolocation,
        on_delete=models.PROTECT,
        help_text="Found location.",
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=None,
        null=True,
        blank=True,
        help_text="Gender of the found people."
    )
    status_condition = models.CharField(
        max_length=5,
        choices=CONDITION_CHOICES,
        default=None,
        blank=True,
        null=True,
        help_text="Status condition of the found people."
    )
