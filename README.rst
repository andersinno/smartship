SmartShip API
=============

Python library to interact with the Posti SmartShip / Unifaun Online API.

TODO
----

* Agent lookups
* Shipment PDF fetching
* Tests
* Docs
* Check schema
* Implement remaining attributes in Shipment as per schema
* Add logging where necessary

Compatibility
-------------

* Python 2.7+ or Python 3.4+

Usage
-----

Creating shipments
~~~~~~~~~~~~~~~~~~

This API supports the Smartship Shipments api for creating shipments and
then downloading the generated PDF's.

Carriers
''''''''

There are methods for certain carriers like Posti to cover more common use
cases. To create a shipment for the Posti carrier, for example:

.. code:: python

    from smartship.carriers.posti import create_shipment
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    sender = {
        "quickId": "1",
    }
    shipment = create_shipment(
        "12345",  # Posti customer number
        "PO2102",  # Service ID
        receiver,
        sender,
        [{"copies": 1}]  # Parcels
     )

See more documentation in ``smartship.carriers.posti`` module.

Client
~~~~~~

To send shipments and use other API resources, you need a client.
Initialize the client as follows with username and secret tokens.  Create
your API tokens in the `Unifaun Online portal
<https://www.unifaunonline.com/>`_.

.. code:: python

    from smartship import Client
    client = Client("username", "secret")

Sending shipments
'''''''''''''''''

Send a shipment as follows:

.. code:: python

    response = client.send_shipment(shipment)

Response will be a standard ``HttpResponse`` object with status code and
content.

Status codes:

* 201 - Shipment was created OK
* 422 - Validation error with the data, see response content

For errors, ``response.content`` has the response JSON with possible error
messages from Unifaun Online API.

Agents
~~~~~~

*TODO: implement agents and address lookups for SmartPost needs*

Advanced usage
~~~~~~~~~~~~~~

See full Smartship `API documentation
<https://smartship.unifaun.com/rs-docs/>`_ for a full list of attributes
that shipments can be given.  All of these are supported when using
``smartship.shipments.Shipment`` directly.  Import the relevant objects
from ``smartship.objects`` and pass them to the ``Shipment`` object.

Development
-----------

Requirements
~~~~~~~~~~~~

Install the requirements to a virtual environment with::

    pip install -U setuptools pip  # These should be up to date
    pip install -r requirements-dev.txt

Tests
~~~~~

To test in the current virtual environment, run::

    py.test

To check the coding style, run::

    flake8

To test all supported environments, run::

    tox

Building documentation
~~~~~~~~~~~~~~~~~~~~~~

Build the documentation with::

    sphinx-build -b html docs docs/_build
