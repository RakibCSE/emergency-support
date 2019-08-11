import logging
import requests

from requests.exceptions import RequestException


def get_ip_address(request):
    """
    Returns ip address
    Args:
        request:

    Returns:
        ip_address: ip address of the requested user.
    """
    ip_address = ""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[-1].strip()
    else:
        ip_url = "https://api.ipify.org"
        try:
            ip_response = requests.get(ip_url)
            if ip_response.status_code == 200:
                ip_address = ip_response.text
        except RequestException as err:
            logging.error(err)

    return ip_address


def get_latlong(ip_address):
    """
    Returns latitude and longitude by ip address.
    Args:
        ip_address (str): User ip address.

    Returns:
        loc_latitude: Latitude
        loc_longitude: Longitude
    """
    loc_latitude = loc_longitude = ""
    latlong_url = "https://ipapi.co/{ip}/latlong/".format(ip=ip_address)
    try:
        response = requests.get(latlong_url)
        if response.status_code == 200:
            response_latlong_list = response.text.split(",")
            loc_latitude, loc_longitude = response_latlong_list[0], response_latlong_list[1]
    except RequestException as err:
        logging.error(err)

    return loc_latitude, loc_longitude


def get_formatted_address(latitude, longitude):
    """
    Return formatted address by location coordinates

    Args:
        latitude (str): Location latitude
        longitude (str): Location longitude

    Returns:
        formatted_address: Formatted address of the location
    """
    formatted_address = ''
    api_key = "d5a602cb251b4d8bacd102f71c3369b8"
    map_url = "https://api.opencagedata.com/geocode/v1/json?key={key}&q={lat},{long}&pretty=1&no_annotations=1".format(
        key=api_key,
        lat=latitude,
        long=longitude
    )
    try:
        map_response = requests.get(map_url)
        if map_response.status_code == 200:
            map_data = map_response.json()
            formatted_address = map_data["results"][0]["formatted"]
    except RequestException as err:
        logging.error(err)

    return formatted_address
