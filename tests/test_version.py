import pkg_resources
from mock import patch
from six.moves import reload_module

import smartship


def test_version():
    assert isinstance(smartship.__version__, str)
    assert '.' in smartship.__version__


@patch('pkg_resources.get_distribution')
def test_version_when_not_installed(get_dist):
    get_dist.side_effect = pkg_resources.DistributionNotFound
    reload_module(smartship)
    assert smartship.__version__ is None
