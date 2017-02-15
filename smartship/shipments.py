# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import attr
import six
from jsonschema import validate

from smartship.client import send
from smartship.objects import Parcels, Receiver, Sender, SenderPartners, Service
from smartship.schemas import REQUEST_SCHEMA


DEFAULT_PDF_CONFIG = {
    "target2YOffset": 0,
    "target1Media": "laser-ste",
    "target1YOffset": 0,
    "target2Media": "laser-a4",
    "target1XOffset": 0,
    "target2XOffset": 0
}


@attr.s
class Shipment(object):
    orderNo = attr.ib(default=None)
    sender = attr.ib(default=Sender())
    senderPartners = attr.ib(default=SenderPartners())
    receiver = attr.ib(default=Receiver())
    parcels = attr.ib(default=Parcels())
    service = attr.ib(default=Service())
    # TODO: add remaining attributes

    _pdf_config = attr.ib(default=DEFAULT_PDF_CONFIG)
    _data = attr.ib(default={})

    def build(self):
        data = {
            "pdfConfig": self._pdf_config,
            "shipment": {
                "sender": self.sender.get_json(),
                "senderPartners": self.senderPartners.get_json(),
                "parcels": self.parcels.get_json(),
                "receiver": self.receiver.get_json(),
                "service": self.service.get_json(),
            }
        }
        if self.orderNo:
            data["shipment"]["orderNo"] = self.orderNo
        # TODO: set remaining attributes, if given
        # Drop top-level key's with empty value
        self._data =  dict((key, value) for key, value in six.iteritems(data) if value)
        validate(self._data, REQUEST_SCHEMA)

    def send(self):
        self.build()
        self.response = send("/shipments", self._data)
        return self.response

    def retrieve_pdfs(self):
        """
        Fetch PDF files using the data in self.response.
        """
        # TODO implement
        return []
