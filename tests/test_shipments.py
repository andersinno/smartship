# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from requests.compat import json


class TestShipment(object):
    def test_shipment_builds(self, simple_shipment):
        simple_shipment.build()
        assert simple_shipment.data == {
            'pdfConfig': {
                'target2YOffset': 0,
                'target2Media': 'laser-a4',
                'target1XOffset': 0,
                'target2XOffset': 0,
                'target1Media': 'laser-ste',
                'target1YOffset': 0
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
                'target2YOffset': 0,
                'target2Media': 'laser-a4',
                'target1XOffset': 0,
                'target2XOffset': 0,
                'target1Media': 'laser-ste',
                'target1YOffset': 0
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
                        }
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
