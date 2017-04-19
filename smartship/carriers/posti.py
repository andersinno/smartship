# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..objects import Agent, Parcels, Receiver, Sender, SenderPartners, Service
from ..shipments import Shipment

CARRIER_CODE = "POSTI"
CARRIER_DESCRIPTION = "Posti Oy, Paketit ja kuljetusyksiköt"

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


def create_shipment(
        custno, service_id, receiver, sender, parcels,
        agent=None, order_no=None, sender_reference=None, addons=None):
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
        sender = {
            "quickId": "1",
        }
        shipment = create_shipment("12345", "PO2102", receiver, sender, [{"copies": 1}])

    :param custno: Posti customer number.
    :type custno: str
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
    :param sender: Sender information. Must either have a 'quickId' or enough address information.
    :type sender: dict
    :param agent: Pickup agent (optional)
    :type agent: dict
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
    :return: Shipment instance
    :rtype: smartship.shipments.Shipment
    """
    _validate_create_shipment(service_id)

    kwargs = {
        "sender": Sender(sender),
        "senderPartners": SenderPartners([{"id": CARRIER_CODE, "custNo": custno}]),
        "receiver": Receiver(receiver),
        "parcels": Parcels(parcels),
        "service": _build_service(addons, service_id),
    }
    if agent:
        kwargs["agent"] = Agent(agent)
    if order_no:
        kwargs["orderNo"] = order_no
    if sender_reference:
        kwargs["senderReference"] = sender_reference

    return Shipment(**kwargs)


def _build_service(addons, service_id):
    service = Service({"id": service_id})
    if addons:
        service["addons"] = addons
    return service


def _validate_create_shipment(service_id):
    if service_id not in SERVICES:
        raise ValueError("Invalid 'service_id'.")
