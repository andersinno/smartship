# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from requests.auth import HTTPBasicAuth

from .constants import ResponseCode


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
        :return: HttpResponse
        """
        shipment.build()
        # TODO: Add logging
        return self._post("/shipments", shipment.data)

    def get_pdf_data(self, shipment_response):
        """
        Fetch PDF-data according to a response to `send_shipment`.

        :param shipment_response: Response to send_shipment call.
        :type shipment_response: requests.models.Response
        :return: PDF-data for each response fragment
        :rtype: list[list[bytes]]
        :raises: ValueError: if the response has the wrong status code for a shipment
        :raises: KeyError: if the the JSON of the response doesn't conform to the schema
        """
        if shipment_response.status_code != ResponseCode.CREATED:
            raise ValueError("Invalid shipment response status code: {!r}".format(
                shipment_response.status_code))

        # TODO: Add logging
        results = []
        for fragment in shipment_response.json():
            result = []
            shipment_id = fragment["id"]
            for pdf in fragment["pdfs"]:
                endpoint = "/shipments/%s/pdfs/%s" % (shipment_id, pdf["id"])
                if not pdf["href"].endswith(endpoint):
                    raise ValueError("PDF href field doesn't match the schema")
                pdf_response = self._get(endpoint)
                if pdf_response.status_code != ResponseCode.OK:
                    raise ValueError("Invalid PDF response status code: {!r}".format(
                        pdf_response.status_code))
                result.append(pdf_response.content)
            results.append(result)
        return results

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
