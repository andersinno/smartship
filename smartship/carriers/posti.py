# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from envparse import env

from smartship.objects import Sender, SenderPartners, Receiver, Service, Parcels
from smartship.shipments import Shipment

CARRIER_CODE = "POSTI"
CARRIER_DESCRIPTION = "Posti Oy, Paketit ja kuljetusyksiköt"

CUSTNO = env("SMARTSHIP_CUSTNO_POSTI", default=None)
DEFAULT_SENDER_QUICKID = env("SMARTSHIP_SENDER_QUICKID", default=None)

SERVICES = {
    "PO2017": "Posti - EMS",
    "PO2017D": "Posti - EMS DocPack",
    "ITKY14I": "Posti - Express Business Day pallet (Ulkomaa)",
    "IT14I": "Posti - Express Business Day parcel (Ulkomaa)",
    "PO2102": "Posti - Express-paketti",
    "PO2144": "Posti - Express-rahti",
    "PO2104": "Posti - Kotipaketti",
    "PO5041": "Posti - Näytelähetys",
    "PO2108": "Posti - Palautus",
    "PO2711": "Posti - Parcel Connect",
    "PO2718": "Posti - Parcel Return Connect",
    "PO2461": "Posti - Pikkupaketti",
    "PO2103": "Posti - Postipaketti",
    "ITPR": "Posti - Priority Parcel",
    "PO2106": "Posti - SmartPOST Viro",
}


def create_shipment(service_id, receiver, parcels, sender=None, order_no=None, sender_reference=None, addons=None,
                    custno=None):
    """
    Create a shipment using the Posti carrier.

    Example simplest case usage:
        receiver = {
            "name": "Anders Innovations",
            "city": "Helsinki",
            "country": "FI",
            "address1": "Iso Roobertinkatu 20-22",
            "zipcode": "00120"
        }
        status_code, content = create_shipment("PO2102", receiver, [{"copies": 1}])

    Returns response status code and content as a tuple. Status codes:
        201 - Shipment was created OK
        422 - Validation error with the data, see response content

    :param service_id: Service to use, see `SERVICES` constant or API documentation.
    :type service_id: str
    :param receiver: Receiver of the shipment. Must either have a 'quickId' or enough address information.
        See example receiver data above. Required receiver information can depend on service chosen. If necessary,
        check service lists in Unifaun Online and API docs at https://smartship.unifaun.com/rs-docs/##creating_shipments
    :type receiver: dict
    :param parcels: Parcels to send in this shipment. This needs to be a list of items, with at minimum the amount
        of items in the parcel. For example, a shipment with one item:
            [
                {
                    "copies": 1,
                },
            ]
        See full specification of in the Smartship API documentation at
        https://smartship.unifaun.com/rs-docs/##creating_shipments
    :type parcels: list
    :param sender: Sender information, define using SMARTSHIP_SENDER_QUICKID env variable or give the quickId or
        full sender information. Has the same fields as `receiver`. (optional, if sender quickId defined via env)
    :type sender: dict
    :param order_no: Order number (optional)
    :type order_no: str
    :param sender_reference: Sender reference (optional)
    :type sender_reference: str
    :param addons: Service addons. Available addons depend on chosen service (optional). See Unfifaun Online
        service lists. Defined as a list of dictionaries containing addon 'id' and additional information, for example:
            [
                {
                    "id": "DNG",
                    "declarant": "Firma Oy",
                },
                {
                    "id": "SPTR",
                },
            ]
    :type addons: list
    :param custno: Posti customer number. Optional if defined via SMARTSHIP_CUSTNO_POSTI env variable.
    :type custno: str
    :return: Response HTTP status code and response content as a tuple
    :rtype: tuple
    """

    _validate_create_shipment(custno, sender, service_id)
    kwargs = {}

    if DEFAULT_SENDER_QUICKID:
        kwargs["sender"] = Sender({"quickId": DEFAULT_SENDER_QUICKID})
    else:
        kwargs["sender"] = Sender(sender)
    kwargs["senderPartners"] = SenderPartners([{"id": CARRIER_CODE, "custNo": custno or CUSTNO}])
    if order_no:
        kwargs["orderNo"] = order_no
    if sender_reference:
        kwargs["senderReference"] = sender_reference
    kwargs["receiver"] = Receiver(receiver)
    service = Service({"id": service_id})
    if addons:
        service["addons"] = addons
    kwargs["service"] = service
    kwargs["parcels"] = Parcels(parcels)

    shipment = Shipment(**kwargs)
    response = shipment.send()

    # TODO: return PDF urls?
    return response.status_code, response.content


def _validate_create_shipment(custno, sender, service_id):
    if not custno and not CUSTNO:
        raise ValueError("Must give 'custno' or define environment variable 'SMARTSHIP_CUSTNO_POSTI'.")
    if not sender and not DEFAULT_SENDER_QUICKID:
        raise ValueError("Must give 'sender' or define environment variable 'SMARTSHIP_SENDER_QUICKID'.")
    if service_id not in SERVICES:
        raise ValueError("Invalid 'service_id'.")
