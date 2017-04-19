# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from requests.auth import HTTPBasicAuth

from .constants import ResponseCode
from .exceptions import ApiError
from .objects import Agents
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

    def get_pdf(self, shipment_id, pdf_id):
        """
        Get specified PDF data for a shipment

        :param shipment_id: Shipment identifier from a shipment response
        :type shipment_id: str
        :param pdf_id: PDF identifier from a shipment response
        :type pdf_id: str
        :return: bytes
        """
        endpoint = "/shipments/%s/pdfs/%s" % (shipment_id, pdf_id)
        pdf_response = self._get(endpoint)
        if pdf_response.status_code != ResponseCode.OK:
            raise ApiError(
                "Invalid PDF response status code: %r" % pdf_response.status_code,
                pdf_response.status_code,
                pdf_response
            )
        return pdf_response.content

    def get_agents(self, country_code, agent_type, street=None, zipcode=None, agent_id=None):
        """
        Get agents (pickup location) information.

        Example using receiver address to get the closest ones:
            agents = client.get_agents("FI", "ITELLASP", "Iso Roobertinkatu 20-22", "00120")
        Example using the agent id:
            agents = client.get_agents("SE", "POSTNORD", agent_id="586181")

        :param country_code: Two letter country code (from ISO-3166-1 alpha-2).
        :type country_code: str
        :param agent_type: Type of the agent. One of
            (SBTL, SBTLFI, PP, PPFI, POSTNORD, DHLSP, DHLSPCOD, GLS, MHM, MHT, ITELLA, ITELLASP, BRING, BUSSGODS, UPS)
        :type agent_type: str
        :param street: The street name and number of the receiver's address for finding the closest agent.
            NOTE: Can't be used with the agent_id parameter.
        :type street: str
        :param zipcode: The zipcode code of the receiver's address. NOTE: Can't be used with the agent_id parameter.
        :type zipcode: str
        :param agent_id: The ID of the agent used by the carrier. NOTE: Can't be used with zipcode or street parameters.
        :type agent_id: str
        :return: Agents
        """
        if agent_id and (street or zipcode):
            raise ValueError("Agent ID and receiver address parameters cannot be used simultaneously")
        params = {
            "countryCode": country_code,
            "type": agent_type,
        }
        if agent_id:
            params["id"] = agent_id
        else:
            params["street"] = street
            params["zip"] = zipcode

        response = self._get("/addresses/agents", params)
        status_code = response.status_code
        if status_code == ResponseCode.MISSING:
            raise ApiError(response.json()["message"], status_code, response)
        elif status_code != ResponseCode.OK:
            raise ApiError("Error getting agents information", status_code, response)

        return Agents(response.json())

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
