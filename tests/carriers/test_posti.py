# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonschema import ValidationError
from mock import patch
from pytest import raises

from smartship.carriers.posti import create_shipment
from smartship.shipments import DEFAULT_PDF_CONFIG, Shipment


@patch("smartship.carriers.posti._validate_create_shipment")
def test_create_shipment(mock_validate):
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    sender = {
        "quickId": "1",
    }
    parcels = [{"copies": 1}]
    shipment = create_shipment("custno", "service_id", receiver, sender, parcels)
    mock_validate.assert_called_once_with("service_id")
    assert isinstance(shipment, Shipment)
    shipment.build()
    assert shipment.data == {
        'pdfConfig': DEFAULT_PDF_CONFIG,
        'shipment': {
            'senderPartners': [
                {
                    'id': 'POSTI',
                    'custNo': 'custno'
                }
            ],
            'receiver': receiver,
            'sender': sender,
            'service': {
                'id': 'service_id'
            },
            'parcels': parcels
        }
    }


@patch("smartship.carriers.posti._validate_create_shipment")
def test_create_more_complex_shipment(mock_validate):
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120",
        "phone": "+358123456789",
        "mobile": "+358123456789",
        "email": "smartship@example.com",
    }
    sender = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120",
        "phone": "+358123456789",
        "mobile": "+358123456789",
        "email": "smartship@example.com",
    }
    parcels = [
        {
            "copies": 1,
            "weight": 2.75,
            "contents": "Awesome things",
        },
        {
            "copies": 5,
            "valuePerParcel": True,
            "dangerousGoods": {
                "unCode": "1234",
                "hazardCode": "1.1",
                "packageCode": "I",
                "description": "Don't set on fire.",
                "adrClass": "1",
                "netWeight": 3.15,
                "trCode": "E",
            }
        },
    ]
    addons = [{"id": "DNG", "declarant": "Anders", }, {"id": "SPTR", }]
    shipment = create_shipment(
        "custno", "service_id", receiver, sender, parcels, order_no="orderno", sender_reference="sender ref",
        pdf_config=DEFAULT_PDF_CONFIG, addons=addons
    )
    mock_validate.assert_called_once_with("service_id")
    assert isinstance(shipment, Shipment)
    shipment.build()
    assert shipment.data == {
        'pdfConfig': DEFAULT_PDF_CONFIG,
        'shipment': {
            'senderPartners': [
                {
                    'id': 'POSTI',
                    'custNo': 'custno'
                }
            ],
            'receiver': receiver,
            'sender': sender,
            'service': {
                'id': 'service_id',
                'addons': addons,
            },
            'parcels': parcels,
            'orderNo': "orderno",
            'senderReference': "sender ref",
        }
    }


@patch("smartship.carriers.posti._validate_create_shipment")
def test_create_invalid_mobile_shipment(mock_validate):
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    sender = {
        "quickId": "1",
    }
    parcels = [{"copies": 1}]
    # Invalid: Missing required "mobile" field.
    with raises(ValidationError):
        create_shipment("custno", "PO2104", receiver, sender, parcels)
    mock_validate.assert_called_once_with("PO2104")


@patch("smartship.carriers.posti._validate_create_shipment")
def test_create_invalid_agent_shipment(mock_validate):
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    sender = {
        "quickId": "1",
    }
    agent = {
        "quickId": "2"
    }
    parcels = [{"copies": 1}]
    # Invalid: Missing required "mobile" field.
    with raises(ValidationError):
        create_shipment("custno", "PO2103", receiver, sender, parcels, agent=agent)
    mock_validate.assert_called_once_with("PO2103")


@patch("smartship.carriers.posti._validate_create_shipment")
def test_create_invalid_parcel_shipment(mock_validate):
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    sender = {
        "quickId": "1",
    }
    parcels = [{"copies": 1}]
    # Invalid: Missing required "weight" field
    with raises(ValidationError):
        create_shipment("custno", "PO5041", receiver, sender, parcels)
    mock_validate.assert_called_once_with("PO5041")
