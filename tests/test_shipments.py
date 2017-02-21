# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import patch

from smartship.client import SmartShipClient


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

    @patch("smartship.shipments.SmartShipClient.send_shipment", return_value="response")
    def test_shipment_send(self, mock_send_shipment, simple_shipment):
        response = simple_shipment.send(("username", "secret"))
        mock_send_shipment.assert_called_once_with(simple_shipment)
        assert response == "response"

    def test_init_client(self, simple_shipment):
        simple_shipment._init_client(("username", "secret"))
        assert isinstance(simple_shipment._client, SmartShipClient)
        assert simple_shipment._client._username == "username"
        assert simple_shipment._client._secret == "secret"
