# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import Mock, patch
from requests.auth import HTTPBasicAuth

from smartship import Client


@patch("smartship._client.requests.post", return_value=Mock(status_code=200))
def test_post(mock_post, smartship_client):
    response = smartship_client._post("/endpoint", data={"data": "value"})
    mock_post.assert_called_once_with(
        "%s%s" % (Client.SMARTSHIP_API_ENDPOINT, "/endpoint"),
        json={"data": "value"},
        auth=HTTPBasicAuth("username", "secret")
    )
    assert response.status_code == 200


@patch("smartship._client.requests.get", return_value=Mock(status_code=200))
def test_get(mock_get, smartship_client):
    response = smartship_client._get("/endpoint", params={"param": "value"})
    mock_get.assert_called_once_with(
        "%s%s" % (Client.SMARTSHIP_API_ENDPOINT, "/endpoint"),
        params={"param": "value"},
        auth=HTTPBasicAuth("username", "secret")
    )
    assert response.status_code == 200


def test_send_shipment(smartship_client, simple_shipment):
    simple_shipment.build()
    simple_shipment.build = Mock()
    smartship_client._post = Mock(return_value="response")
    response = smartship_client.send_shipment(simple_shipment)
    simple_shipment.build.assert_called_once_with()
    smartship_client._post.assert_called_once_with("/shipments", simple_shipment.data)
    assert response == "response"
