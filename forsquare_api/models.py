from django.db import models


class Location(models.Model):
    fsq_id = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.TextField(null=True)
    country = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.country + '-' + self.name

