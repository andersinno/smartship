# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from mock import patch, Mock
from requests.auth import HTTPBasicAuth

from smartship import settings
from smartship.client import send


@patch("smartship.client.requests.post", return_value=Mock(status_code=200))
def test_send(mock_post):
    response = send("/foo", data={"foo": "bar"})
    mock_post.assert_called_once_with(
        "%s%s" % (settings.SMARTSHIP_API_ENDPOINT, "/foo"),
        data=json.dumps({"foo": "bar"}).encode("UTF-8"),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth("username", "secret")
    )
    assert response.status_code == 200
