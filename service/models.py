from django.db import models


class ServiceSeeker(models.Model):
    loc_latitude = models.FloatField(null=False)
    loc_longitude = models.FloatField(null=False)
    seeker_ip = models.GenericIPAddressField(null=False)

    def __str__(self):
        return self.seeker_ip
