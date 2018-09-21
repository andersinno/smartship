# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import attr
import six
from jsonschema import validate

from .constants import ResponseCode
from .exceptions import ApiError
from .objects import (
    Agent, Parcels, PDFConfig, Receiver, Sender, SenderPartners, Service)
from .schemas import REQUEST_SCHEMA

DEFAULT_PDF_CONFIG = {
    "target1Media": "laser-a5",
    "target1YOffset": 0,
    "target1XOffset": 0,
}


@attr.s
class Shipment(object):
    agent = attr.ib(default=Agent())
    orderNo = attr.ib(default=None)
    sender = attr.ib(default=Sender())
    senderPartners = attr.ib(default=SenderPartners())
    receiver = attr.ib(default=Receiver())
    parcels = attr.ib(default=Parcels())
    service = attr.ib(default=Service())
    senderReference = attr.ib(default="")
    freeText1 = attr.ib(default="")
    # TODO: add remaining attributes

    data = attr.ib(default={})
    pdfConfig = attr.ib(default=PDFConfig())

    def build(self):
        """
        Build and validate the data for a Shipment.
        """
        data = {
            "shipment": {
                "sender": self.sender.get_json(),
                "senderPartners": self.senderPartners.get_json(),
                "parcels": self.parcels.get_json(),
                "receiver": self.receiver.get_json(),
                "service": self.service.get_json(),
            }
        }
        pdf_config = self.pdfConfig.get_json()
        data["pdfConfig"] = pdf_config if pdf_config else DEFAULT_PDF_CONFIG
        agent = self.agent.get_json()
        if agent:
            data["shipment"]["agent"] = agent
        if self.orderNo:
            data["shipment"]["orderNo"] = self.orderNo
        if self.senderReference:
            data["shipment"]["senderReference"] = self.senderReference
        if self.freeText1:
            data["shipment"]["freeText1"] = self.freeText1
        # TODO: set remaining attributes, if given
        # Drop top-level key's with empty value
        self.data = dict((key, value) for key, value in six.iteritems(data) if value)
        validate(self.data, REQUEST_SCHEMA)


class ShipmentResponseError(ApiError):
    pass


class ShipmentResponse(object):
    def __init__(self, response):
        try:
            self.response_code = ResponseCode(response.status_code)
        except ValueError:
            raise ValueError("Unknown response status %d" % response.status_code)
        self.raw = response

    def raise_for_status(self):
        error_message = None
        if self.response_code is ResponseCode.MISSING:
            error_message = "Missing required attribute: %s" % self.raw.json()["message"]
        elif self.response_code is ResponseCode.UNAUTHORIZED:
            error_message = "Unauthorized API use: %s" % self.raw.reason
        elif self.response_code is ResponseCode.VALIDATION_ERROR:
            fields = ",".join(str(error["field"]) for error in self.raw.json())
            error_message = "Validation failed on fields: %s" % fields
        elif self.response_code is ResponseCode.SERVER_ERROR:
            try:
                data = self.raw.json()
                if "message" not in data:
                    error_message = "Invalid server response"
                else:
                    error_message = "Internal server error: %s" % data["message"]
            except ValueError as e:
                error_message = str(e)

        if error_message is not None:
            raise ShipmentResponseError(error_message, self.response_code, self.raw)

    def get_pdfs(self, client):
        """
        Extract PDF data from the response or fetch it if missing.

        :param client: Smartship client with valid credentials
        :type client: smartship.Client
        :return: PDF-data for each response fragment
        :rtype: list[list[bytes]]
        :raises: ShipmentResponseError: if the response has the wrong status code for a shipment
        :raises: KeyError: if the the JSON of the response doesn't conform to the schema
        """
        if self.response_code != ResponseCode.CREATED:
            raise ShipmentResponseError(
                "Invalid shipment response status code: %r" % self.response_code, self.response_code, self.raw
            )

        # TODO: Add logging
        results = []
        for fragment in self.raw.json():
            result = []
            shipment_id = fragment["id"]
            for pdf in fragment["pdfs"]:
                # Check if PDF data was already included in the response
                if pdf.get("pdf"):
                    # Use existing data
                    result.append(pdf["pdf"])
                else:
                    # Fetch missing data
                    result.append(client.get_pdf(shipment_id, pdf["id"]))
            results.append(result)
        return results

    @property
    def data(self):
        return self.raw.json()
