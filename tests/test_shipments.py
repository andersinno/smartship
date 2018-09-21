# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from requests.compat import json


class TestShipment(object):
    def test_shipment_builds(self, simple_shipment):
        simple_shipment.build()
        assert simple_shipment.data == {
            'pdfConfig': {
                'target1Media': 'laser-a5',
                'target1YOffset': 0,
                'target1XOffset': 0
            },
            'shipment': {
                'sender': {
                    'quickId': '1'
                },
                'service': {
                    'id': 'SER'
                },
                'senderPartners': [
                    {
                        'id': 'PAR'
                    }
                ],
                'receiver': {
                    'city': 'HELSINKI',
                    'name': 'Foo Bar',
                    'country': 'FI'
                },
                'orderNo': '123',
                'parcels': [
                    {
                        'copies': 1
                    }
                ]
            }
        }

    def test_complex_shipment_builds(self, complex_shipment):
        complex_shipment.build()
        assert complex_shipment.data == {
            'pdfConfig': {
                'target1Media': 'laser-2a5',
                'target1YOffset': 1,
                'target1XOffset': 1
            },
            'shipment': {
                'sender': {
                    'quickId': '1'
                },
                'service': {
                    'id': 'SER',
                    'addons': [
                        {
                            'id': 'DNG',
                            'declarant': 'Company Inc.'
                        },
                        {
                            'id': 'SPTR'
                        },
                        {
                            'id': 'COD',
                            'amount': Decimal('1.25'),
                            'account': 'FI2112345600000785',
                            'bank': 'DEVBANKX',
                            'currencyCode': 'EUR',
                        },
                    ],
                },
                'senderPartners': [
                    {
                        'id': 'PAR',
                        'custNo': '1'
                    }
                ],
                'receiver': {
                    'quickId': '2'
                },
                'orderNo': '456',
                'freeText1': 'This is some sample free text here.',
                'senderReference': '789',
                'parcels': [
                    {
                        'copies': 1,
                        'weight': Decimal('1.23'),
                        'volume': Decimal('45.6'),
                        'contents': 'Stuff',
                        'valuePerParcel': True,
                        'dangerousGoods': {
                            'unCode': '1234',
                            'hazardCode': '1.1',
                            'packageCode': 'I',
                            'description': 'Dangerous stuff',
                            'adrClass': '1',
                            'netWeight': Decimal('1.23'),
                            'trCode': 'E'
                        },
                    }
                ],
                'agent': {
                    'city': 'HELSINKI',
                    'name': 'Foo Bar',
                    'country': 'FI'
                }
            }
        }

    def test_complex_shipment_serializes(self, complex_shipment):
        """
        Test that requests can send data with Decimal values.
        """
        complex_shipment.build()
        json.dumps(complex_shipment.data)
