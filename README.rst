SmartShip API
=============

Python library to interact with the Posti SmartShip / Unifaun Online API.

TODO
----

* Docs
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
    agent = {
        "quickId": "2",
    }
    shipment = create_shipment(
        "12345",  # Posti customer number
        "PO2102",  # Service ID
        receiver,
        sender,
        [{"copies": 1}],  # Parcels
        agent=agent,  # Optional pickup point
        pdf_config=pdf_config,  # Optional custom PDF config
     )

See more documentation in ``smartship.carriers.posti`` module.

PDF Config
''''''''''

If you want to pass a custom ``pdf_config``, it should have the following structure:

.. code:: python

    {
    "target1Media": "laser-a5",
    "target1YOffset": 0,
    "target1XOffset": 0
    }

With ``"target1Media"`` being one of the following options::

    "laser-a5"
    "laser-2a5"
    "laser-ste"
    "thermo-se"
    "thermo-225"

You can customize the offset with ``"target1YOffset"`` and ``"target1XOffset"`` parameters.

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

Response will be a special ``ShipmentResponse`` wrapping a ``HttpResponse`` object with response code and
JSON content in ``response.data``.

Status codes:

* 201 - Shipment was created OK
* 422 - Validation error with the data. Raises a ``ShipmentResponseError``.

For errors see ``error.response.json()`` for details from Unifaun Online API.

Shipment address PDF slips
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the response retrieve associated PDF data as follows:

.. code:: python

    data = response.get_pdfs(client)  # Client needed in case of additional fetching
    pdf_data = data[0][0]  # Simplest case with a single shipment with a single parcel

Agents
~~~~~~

Retrieve a list of agents (pickup points) as follows:

.. code:: python

    agents = client.get_agents("FI", "ITELLASP", "Iso Roobertinkatu 20-22", "00120")

Response will be an ``Agents`` object that can be iterated over for individual agent data.

Locations
~~~~~~~~~

As the above agents method is a paid service we also provide an interface to the Posti location service API.

.. code:: python

    from smartship.carriers.posti import get_locations
    locations = get_locations(country_code="FI", zipcode="00120")

Response will be a ``Locations`` object that can be iterated over for individual location data.

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
