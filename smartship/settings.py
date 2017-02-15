# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from envparse import env


SMARTSHIP_API_ENDPOINT = env("SMARTSHIP_API_ENDPOINT", default="https://api.unifaun.com/rs-extapi/v1")

# These must be defined or API calls will fail
SMARTSHIP_API_USERNAME = env("SMARTSHIP_API_USERNAME", default="")
SMARTSHIP_API_SECRET = env("SMARTSHIP_API_SECRET", default="")
