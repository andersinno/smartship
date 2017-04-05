# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import Mock, patch
from pytest import raises
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


@patch("smartship._client.requests.get", return_value=Mock(status_code=200, content="pdfdata"))
def test_get_pdf_data(mock_get, smartship_client):
    href = "%s/shipments/%d/pdfs/%d" % (Client.SMARTSHIP_API_ENDPOINT, 1, 2)
    content = [{
        "id": 1,
        "pdfs": [{
            "id": 2,
            "href": href,
        }],
    }]
    response = Mock(status_code=201)
    response.json = Mock(return_value=content)
    pdf_data = smartship_client.get_pdf_data(response)
    assert pdf_data == [["pdfdata"]]
    mock_get.assert_called_once_with(
        href,
        params=None,
        auth=HTTPBasicAuth("username", "secret")
    )


def test_get_pdf_data_fail(smartship_client):
    with raises(ValueError):
        smartship_client.get_pdf_data(Mock(status_code=200))
