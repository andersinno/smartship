# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
