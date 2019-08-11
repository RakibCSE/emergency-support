from rest_framework import serializers

from service.models import ServiceSeeker


class ServiceSeekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceSeeker
        fields = ('loc_latitude', 'loc_longitude', 'seeker_ip')
