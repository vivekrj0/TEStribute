"""
To deal with all distance calculations needed by the TESTribute
"""
import socket
from typing import Dict
from urllib.parse import urlparse

from geopy.distance import geodesic
from ip2geotools.databases.noncommercial import DbIpCity


def return_distance(ip1: str, ip2: str) -> Dict:
    """
    :param ip1: string ip/url
    :param ip2: string ip/url
    :return: a dict containing the locations of both input addresses &
    the physical distance between them in km's
    """
    # to-do :
    #       except error for localhost

    ip1 = DbIpCity.get(socket.gethostbyname(urlparse(ip1).netloc), api_key="free")
    ip2 = DbIpCity.get(socket.gethostbyname(urlparse(ip2).netloc), api_key="free")

    coords_1 = (ip1.latitude, ip1.longitude)
    coords_2 = (ip2.latitude, ip2.longitude)
    return {
        "source": {
            "city": ip1.city,
            "region": ip1.region,
            "country": ip1.country,
        },
        'destination': {
            'city': ip2.city,
            'region': ip2.region,
            'country': ip2.country,
        },
        'distance': geodesic(coords_1, coords_2).km,
    }
