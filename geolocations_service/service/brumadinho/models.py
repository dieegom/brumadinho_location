from django.db import models


class Geolocation(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str("lat: {} long: {}".format(
            self.latitude,
            self.longitude
        ))


class VisitedLocation(models.Model):

    reference = models.CharField(max_length=100)
    location = models.ForeignKey(Geolocation, on_delete=models.PROTECT)
    radius = models.PositiveIntegerField(
        "Approx. radius visited from marker", blank=True, default=1)
    date_visited = models.DateTimeField("Date of Visit", auto_now_add=True)
    notes = models.TextField("Visit Notes",
                            max_length=255,
                            blank=True,
                            null=True)
