# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

import pytest
from mock import Mock

from smartship import Client
from smartship.objects import (
    Agent, Parcels, PDFConfig, Receiver, Sender, SenderPartners, Service)
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
def complex_shipment():
    return Shipment(
        orderNo="456",
        freeText1="This is some sample free text here.",
        senderReference="789",
        sender=Sender({
            "quickId": "1",
        }),
        senderPartners=SenderPartners([{
            "id": "PAR",
            "custNo": "1"
        }]),
        parcels=Parcels([{
            "copies": 1,
            "weight": Decimal("1.23"),
            "volume": Decimal("45.6"),
            "contents": "Stuff",
            "valuePerParcel": True,
            "dangerousGoods": {
                "unCode": "1234",
                "hazardCode": "1.1",
                "packageCode": "I",
                "description": "Dangerous stuff",
                "adrClass": "1",
                "netWeight": Decimal("1.23"),
                "trCode": "E"
            },
        }]),
        receiver=Receiver({
            "quickId": "2",
        }),
        service=Service({
            "id": "SER",
            "addons": [
                {
                    "id": "DNG",
                    "declarant": "Company Inc."
                },
                {
                    "id": "SPTR"
                },
                {
                    'id': 'COD',
                    'amount': Decimal('1.25'),
                    'account': 'FI2112345600000785',
                    'bank': 'DEVBANKX',
                    'currencyCode': 'EUR',
                },
            ],
        }),
        agent=Agent({
            "name": "Foo Bar",
            "city": "HELSINKI",
            "country": "FI",
        }),
        pdfConfig=PDFConfig({
            "target1Media": "laser-2a5",
            "target1YOffset": 1,
            "target1XOffset": 1
        }),
    )


@pytest.fixture
def smartship_client():
    return Client("username", "secret")


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
