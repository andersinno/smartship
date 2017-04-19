# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from requests.auth import HTTPBasicAuth

from .shipments import ShipmentResponse


class Client(object):
    """
    Used for communicating with the Unifaun Online REST API.
    """
    SMARTSHIP_API_ENDPOINT = "https://api.unifaun.com/rs-extapi/v1"

    def __init__(self, username, secret, api_url=None):
        self._username = username
        self._secret = secret
        if api_url:
            self._api_url = api_url
        else:
            self._api_url = self.SMARTSHIP_API_ENDPOINT

    def send_shipment(self, shipment):
        """
        Build and send a Shipment.

        :param shipment: Shipment instance
        :type shipment: smartship.shipments.Shipment
        :return: ShipmentResponse
        """
        shipment.build()
        # TODO: Add logging
        response = self._post("/shipments", shipment.data)
        shipment_response = ShipmentResponse(response)
        shipment_response.raise_for_status()
        return shipment_response

    def _post(self, endpoint, data):
        """
        Send a post request to the Posti SmartShip/Unifaun API.

        :param endpoint: API endpoint for desired API resource (for example `/shipments`)
        :type endpoint: string
        :type data: dict
        :return: response received from Posti SmartShip/Unifaun
        :rtype: HttpResponse
        """
        response = requests.post(
            "%s%s" % (self._api_url, endpoint),
            json=data,
            auth=HTTPBasicAuth(self._username, self._secret)
        )
        # TODO: Add error logging
        return response

    def _get(self, endpoint, params=None):
        """
        Get a resource from the Posti SmartShip/Unifaun API.

        :param endpoint: API endpoint for desired API resource (for example `/shipments/<id>/pdfs`)
        :type endpoint: string
        :type params: dict
        :return: response received from Posti SmartShip/Unifaun
        :rtype: HttpResponse
        """
        response = requests.get(
            "%s%s" % (self._api_url, endpoint),
            params=params,
            auth=HTTPBasicAuth(self._username, self._secret),
        )
        # TODO: Add logging
        return response
