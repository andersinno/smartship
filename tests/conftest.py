# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from mock import Mock

from smartship.client import SmartShipClient
from smartship.objects import Sender, SenderPartners, Parcels, Receiver, Service
from smartship.shipments import Shipment


@pytest.fixture
def simple_shipment():
    return Shipment(
        orderNo="123",
        sender=Sender({
            "quickId": "1",
        }),
        senderPartners=SenderPartners([{
            "id": "PAR",
        }]),
        parcels=Parcels([{
            "copies": 1,
        }]),
        receiver=Receiver({
            "name": "Foo Bar",
            "city": "HELSINKI",
            "country": "FI",
        }),
        service=Service({
            "id": "SER",
        })
    )


@pytest.fixture
def smartship_client():
    return SmartShipClient(("username", "secret"))


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Disable requests calls."""
    monkeypatch.setattr("requests.post", Mock())

    class MockResponse(str):
        status_code = 200
        text = ""

        @staticmethod
        def raise_for_status():
            pass

    monkeypatch.setattr("requests.get", Mock(return_value=MockResponse))
