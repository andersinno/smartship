# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonschema import ValidationError
from mock import Mock, patch
from pytest import raises

from smartship.carriers.posti import (
    LOCATION_SERVICE_API_ENDPOINT, create_shipment, get_additional_services,
    get_locations)
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


LOCATION = {
    "publicName": {
        "fi": "Posti, Keskusta",
        "en": "Posti, Keskusta",
        "sv": "Posti, Keskusta"
    },
    "openingTimes": [
        {
            "timeFromWithPoint": "08.00",
            "timeFrom": "08:00",
            "weekday": "1",
            "timeTo": "20:00",
            "timeToWithPoint": "20.00"
        },
        {
            "timeFromWithPoint": "08.00",
            "timeFrom": "08:00",
            "weekday": "2",
            "timeTo": "20:00",
            "timeToWithPoint": "20.00"
        },
        {
            "timeFromWithPoint": "08.00",
            "timeFrom": "08:00",
            "weekday": "3",
            "timeTo": "20:00",
            "timeToWithPoint": "20.00"
        },
        {
            "timeFromWithPoint": "08.00",
            "timeFrom": "08:00",
            "weekday": "4",
            "timeTo": "20:00",
            "timeToWithPoint": "20.00"
        },
        {
            "timeFromWithPoint": "08.00",
            "timeFrom": "08:00",
            "weekday": "5",
            "timeTo": "20:00",
            "timeToWithPoint": "20.00"
        },
        {
            "timeFromWithPoint": "10.00",
            "timeFrom": "10:00",
            "weekday": "6",
            "timeTo": "15:00",
            "timeToWithPoint": "15.00"
        }
    ],
    "postalOfficeType": None,
    "pupCode": "201003200",
    "lastEmptyTime": None,
    "labelName": {
        "fi": "c/o Posti, Keskusta",
        "en": "c/o Posti, Keskusta",
        "sv": "c/o Posti, Keskusta"
    },
    "dropOfTimeExpress": "17:00:00",
    "availability": "ma-pe 8.00 - 20.00, la 10.00 - 15.00",
    "postalCodeAreas": [
        "20100",
        "20101",
        "20173",
        "20200",
        "20204"
    ],
    "category": None,
    "additionalInfo": {
        "fi": "Helatorstai 10.5.2018 suljettu",
        "en": "",
        "sv": ""
    },
    "capacity": "0",
    "countryCode": "FI",
    "id": "295",
    "location": {
        "lat": "60.4494938297",
        "lon": "22.2625354699"
    },
    "postalCode": "20100",
    "dropOfTimeParcel": "17:00:00",
    "wheelChairAccess": False,
    "routingServiceCode": "3200",
    "address": {
        "fi": {
            "postalCodeName": "TURKU",
            "municipality": "Turku",
            "streetNumber": "19",
            "address": "Eerikinkatu 19",
            "postalCode": "20100",
            "streetName": "Eerikinkatu"
        },
        "en": {
            "postalCodeName": "TURKU",
            "municipality": "Turku",
            "streetNumber": "19",
            "address": "Eerikinkatu 19",
            "postalCode": "20100",
            "streetName": "Eerikinkatu"
        },
        "sv": {
            "postalCodeName": "ÅBO",
            "municipality": "åbo",
            "streetNumber": "19",
            "address": "Eriksgatan 19",
            "postalCode": "20100",
            "streetName": "Eriksgatan"
        }
    },
    "letterClass": None,
    "emptyTime": None,
    "type": "POSTOFFICE",
    "locationName": {
        "fi": "Centrum",
        "en": "",
        "sv": ""
    },
    "partnerType": "POSTI",
    "dropOfTimeLetters": "17:00:00"
}


@patch("smartship.carriers.posti.requests.get", return_value=Mock(json=lambda: {"locations": [LOCATION]}))
def test_get_locations(mock_get):
    locations = get_locations(zipcode="20100")
    assert len(list(locations)) == 1
    assert locations[0]["type"] == "POSTOFFICE"
    mock_get.assert_called_once_with(LOCATION_SERVICE_API_ENDPOINT, params={"zipCode": "20100"})


def test_additional_services():
    additional_services = get_additional_services("PO2103")
    assert len(additional_services) == 14
    assert additional_services["COD"] == "Postiennakko"
