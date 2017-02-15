# SmartShip API

Python library to interact with the Posti SmartShip API.

## TODO:

* Agent lookups
* Shipment PDF fetching
* Tests
* Docs
* Check schema
* Implement remaining attributes in Shipment as per schema
* Add logging where necessary

## Compatibility

* Python 2.7+ or Python 3.4+

## Usage

### Authentication

Username and secret API tokens must be set as environment variables. Create your API tokens in the [Unifaun Online portal](https://www.unifaunonline.com/).

    export SMARTSHIP_API_USERNAME=1234567890
    export SMARTSHIP_API_SECRET=0987654321

### Creating shipments

This API supports the Smartship Shipments api for creating shipments and then downloading the generated PDF's.

#### Configuration

Some defaults can be set as environment variables, though they are optional. If they are not set, they must be given when creating shipments.

    # Default sender quickId to use
    export SMARTSHIP_SENDER_QUICKID=1
    
    # Default Posti customer number (Posti only)
    export SMARTSHIP_CUSTNO_POSTI=123456

#### Carriers

There are methods for certain carriers like Posti to cover more common use cases. To use the Posti carrier, for example:

    from smartship.carriers.posti import create_shipment
    receiver = {
        "name": "Anders Innovations",
        "city": "Helsinki",
        "country": "FI",
        "address1": "Iso Roobertinkatu 20-22",
        "zipcode": "00120"
    }
    status_code, content = create_shipment("PO2102", receiver, [{"copies": 1}])

See more documentation in `smartship.carriers.posti` module. 

### Agents

    # TODO implement agents and address lookups for SmartPost needs

#### Advanced usage

See full Smartship [API documentation](https://smartship.unifaun.com/rs-docs/) for a full list of attributes that shipments can be given. All of these are supported when using `smartship.shipments.Shipment` directly. Import the relevant objects from `smartship.objects` and pass them to the `Shipment` object.

## Development

### Requirements

    pip install -e .
    pip install -U -r dev-requirements.txt
    
### Tests

    py.test

### Building documentation

    sphinx-build -b html docs docs/_build
