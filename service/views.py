import json
import logging

import requests

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service import utils
from service.models import ServiceSeeker
from service.serializers import ServiceSeekerSerializer


# Setting up logging
LOG_FORMAT = "%(asctime)s > %(levelname)s > Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="test.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w",)
logger = logging.getLogger(__name__)


class ServiceSeekerList(generics.ListAPIView):
    """
    Returns models instance list
    """
    queryset = ServiceSeeker.objects.all()
    serializer_class = ServiceSeekerSerializer


def home(request):
    """
    Return response to the homepage
    Args:
        request:

    Returns:
        response:
    """
    response = render(request, "service/home.html")
    return response


@api_view(['POST'])
def get_service(request):
    """
    Save post data to the model.
    Args:
        request (object):

    Returns:
        response (object): Return address data JsonResponse if POST request, else render to homepage.
    """

    data = {}
    address_data = {}
    if request.POST:
        post_data = request.POST
        loc_latitude = post_data.get('loc_latitude', "")
        loc_longitude = post_data.get('loc_longitude', "")
        ip_address = utils.get_ip_address(request)

        # Check if latitude and longitude are not present
        if not (loc_latitude and loc_longitude):
            loc_latitude, loc_longitude = utils.get_latlong(ip_address)

        if loc_latitude and loc_longitude:
            formatted_address = utils.get_formatted_address(loc_latitude, loc_longitude)

            if formatted_address:
                address_data = {
                    "formatted_address": formatted_address,
                    "latitude": loc_latitude,
                    "longitude": loc_longitude
                }
                data = {
                    "loc_latitude": loc_latitude,
                    "loc_longitude": loc_longitude,
                    "seeker_ip": ip_address
                }
                serializer = ServiceSeekerSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        response = JsonResponse(json.dumps(address_data), safe=False)
        return response
    else:
        response = render(request, "service/home.html")
        return response
