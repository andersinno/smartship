# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import Mock, patch
from pytest import raises
from requests.auth import HTTPBasicAuth

from smartship import Client
from smartship.constants import ResponseCode
from smartship.exceptions import ApiError
from smartship.objects import Agents
from smartship.shipments import ShipmentResponse, ShipmentResponseError


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
    data = [{"parcels": [{"parcelNo": "1234"}]}]
    mock_response = Mock(status_code=201, json=lambda: data)
    smartship_client._post = Mock(return_value=mock_response)
    response = smartship_client.send_shipment(simple_shipment)
    simple_shipment.build.assert_called_once_with()
    smartship_client._post.assert_called_once_with("/shipments", simple_shipment.data)
    assert response.raw is mock_response
    assert response.response_code is ResponseCode.CREATED
    assert response.data == data


def test_send_shipment_error(smartship_client, simple_shipment):
    simple_shipment.build()
    simple_shipment.build = Mock()
    mock_content = {
        ResponseCode.MISSING: {"message": "Missing zipcode"},
        ResponseCode.UNAUTHORIZED: None,
        ResponseCode.VALIDATION_ERROR: [{"field": "zipcode"}, {"field": "city"}],
        ResponseCode.SERVER_ERROR: {"message": "Internal server error"},
        ResponseCode.SERVER_ERROR: "Internal error",
        481: None,
    }
    for code, content in mock_content.items():
        def mock_json():
            if content == "Internal error":
                raise ValueError("No JSON object could be decoded")
            return content
        mock_response = Mock(status_code=int(code), json=mock_json, reason="Unauthorized")
        smartship_client._post = Mock(return_value=mock_response)
        try:
            smartship_client.send_shipment(simple_shipment)
        except ShipmentResponseError as e:
            assert e.response is mock_response
            assert e.code is code
        except ValueError as e:
            assert code == 481


@patch("smartship._client.requests.get", return_value=Mock(status_code=200, content=b"pdfdata"))
def test_get_pdf_data(mock_get, smartship_client):
    href = "%s/shipments/%d/pdfs/%d" % (Client.SMARTSHIP_API_ENDPOINT, 1, 2)
    content = [
        {
            "id": 1,
            "pdfs": [{
                "id": 2,
                "href": href,
            }],
        },
        {
            "id": 2,
            "pdfs": [{
                "id": 3,
                "pdf": b"existingdata",
            }],
        }
    ]
    response = Mock(status_code=201)
    response.json = Mock(return_value=content)
    shipment_response = ShipmentResponse(response)
    pdf_data = shipment_response.get_pdfs(smartship_client)
    assert pdf_data == [[b"pdfdata"], [b"existingdata"]]
    mock_get.assert_called_once_with(
        href,
        params=None,
        auth=HTTPBasicAuth("username", "secret")
    )


def test_get_pdf_data_fail(smartship_client):
    with raises(ShipmentResponseError):
        shipment_response = ShipmentResponse(Mock(status_code=200))
        shipment_response.get_pdfs(smartship_client)


def test_get_agents(smartship_client):
    smartship_client._get = lambda *args: Mock(
        status_code=200, json=lambda:
            [{
              "id": "1",
              "name": "Supermarket",
              "address1": "Teststreet 9",
              "address2": None,
              "zipcode": "00120",
              "city": "HELSINKI",
              "state": None,
              "countryCode": "FI",
              "contact": None,
              "phone": None,
              "fax": None,
              "email": None,
              "sms": None,
              "serviceType": None,
              "serviceCode": None,
              "openingHours": None
            }]
    )
    agents = smartship_client.get_agents("FI", "ITELLASP", "Teststreet 10", "00120")
    assert isinstance(agents, Agents)
    data = agents.get_json()
    assert data[0]["id"] == "1"


def test_get_agents_bad_args(smartship_client):
    smartship_client._get = Mock()
    with raises(ValueError):
        smartship_client.get_agents("FI", "ITELLA", "Teststreet 10", "00120", agent_id="1234")


def test_get_agents_illegal_type(smartship_client):
    smartship_client._get = lambda *args: Mock(
        status_code=400, json=lambda:
            {'code': 'ILLEGAL_ARG', 'message': 'Illegal type argument'}
    )
    try:
        smartship_client.get_agents("FI", "FOO", agent_id="123")
    except ApiError as e:
        assert e.args[0] == 'Illegal type argument'
        assert e.code == ResponseCode.MISSING
    else:
        assert False
