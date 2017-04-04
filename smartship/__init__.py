import pkg_resources

from ._client import Client

__author__ = "Anders Innovations"

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = None

__all__ = [
    'Client',
]
