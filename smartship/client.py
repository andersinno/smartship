# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from requests.auth import HTTPBasicAuth

from smartship import settings


def get_username_and_secret():
    username, secret = settings.SMARTSHIP_API_USERNAME, settings.SMARTSHIP_API_SECRET
    if not username or not secret:
        raise Exception("SMARTSHIP_API_USERNAME and SMARTSHIP_API_SECRET must be defined!")
    return username, secret


def send(endpoint, data):
    """
    Send data to Posti SmartShip/Unifaun API

    :param endpoint: API endpoint for desired API resource (for example `/shipments`)
    :type endpoint: string
    :type data: dict
    :return: response received from Posti SmartShip/Unifaun
    :rtype: HttpResponse
    """
    username, secret = get_username_and_secret()
    response = requests.post(
        "%s%s" % (settings.SMARTSHIP_API_ENDPOINT, endpoint),
        data=json.dumps(data).encode("UTF-8"),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(username, secret)
    )
    # TODO: Add logging
    return response


def get_resource(endpoint, params=None, stream=False):
    """

    :param endpoint: API endpoint for desired API resource (for example `/shipments`)
    :type endpoint: string
    :return: response received from Posti SmartShip/Unifaun
    :rtype: HttpResponse
    """
    username, secret = get_username_and_secret()
    response = requests.get(
        "%s%s" % (settings.SMARTSHIP_API_ENDPOINT, endpoint),
        params=params,
        auth=HTTPBasicAuth(username, secret),
        stream=stream
    )
    return response
