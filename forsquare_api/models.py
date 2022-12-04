from django.db import models


class Location(models.Model):
    fsq_id = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.country + '-' + self.name
