from __future__ import unicode_literals

CUSTOMS_DECLARATION_SCHEMA = {
    "type": "object",
    "properties": {
        "sender": {
            "type": "object",
            "required": ["name", "city", "country"],
            "properties": {
                "quickId": {"type": "string"},
                "orgNo": {"type": "string"},
                "vatNo": {"type": "string"},
                "name": {"type": "string"},
                "address1": {"type": "string"},
                "address2": {"type": "string"},
                "zipcode": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "country": {"type": "string"},
                "contact": {"type": "string"},
                "phone": {"type": "string"},
                "fax": {"type": "string"},
                "email": {"type": "string"},
                "mobile": {"type": "string"},
                "doorCode": {"type": "string"},
                "serviceType": {"type": "string"},
                "serviceCode": {"type": "string"},
                "openingHours": {"type": "string"}
            }
        },
        "receiver": {
            "type": "object",
            "required": ["name", "city", "country"],
            "properties": {
                "quickId": {"type": "string"},
                "orgNo": {"type": "string"},
                "vatNo": {"type": "string"},
                "name": {"type": "string"},
                "address1": {"type": "string"},
                "address2": {"type": "string"},
                "zipcode": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "country": {"type": "string"},
                "contact": {"type": "string"},
                "phone": {"type": "string"},
                "fax": {"type": "string"},
                "email": {"type": "string"},
                "mobile": {"type": "string"},
                "doorCode": {"type": "string"},
                "serviceType": {"type": "string"},
                "serviceCode": {"type": "string"},
                "openingHours": {"type": "string"}
            }
        },
        "printSet": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "parcelCount": {"type": "integer", "minimum": 0},
        "reference": {"type": "string"},
        "sourceCountryCode": {"type": "string"},
        "destinationCountryCode": {"type": "string"},
        "shippingCodeBorder": {"type": "string"},
        "shippingCodeDomestic": {"type": "string"},
        "finance1": {"type": "string"},
        "finance2": {"type": "string"},
        "declarantCity": {"type": "string"},
        "declarantDate": {"type": "string"},
        "declarant": {"type": "string"},
        "jobTitle": {"type": "string"},
        "edocNormal": {"type": "boolean"},
        "representative1": {"type": "string"},
        "representative2": {"type": "string"},
        "representativeOrgNo": {"type": "string"},
        "invoiceType": {"type": "string"},
        "invoiceNo": {"type": "string"},
        "discount": {"type": "number", "minimum": 0},
        "freightCharges": {"type": "number", "minimum": 0},
        "insuranceCharges": {"type": "number", "minimum": 0},
        "otherCharges": {"type": "number", "minimum": 0},
        "exportLicenseNo": {"type": "string"},
        "exportDeclaration1": {"type": "string"},
        "exportDeclaration2": {"type": "string"},
        "generalNote1": {"type": "string"},
        "generalNote2": {"type": "string"},
        "generalNote3": {"type": "string"},
        "generalNote4": {"type": "string"},
        "currencyCode": {"type": "string"},
        "importExportType": {"type": "string"},
        "invoiceDeclaration1": {"type": "string"},
        "invoiceDeclaration2": {"type": "string"},
        "importLicenseNo": {"type": "string"},
        "certificate": {"type": "string"},
        "explanation": {"type": "string"},
        "termCode": {"type": "string"},
        "termLocation": {"type": "string"},
        "lines": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["copies"],
                "properties": {
                    "valuesPerItem": {"type": "boolean"},
                    "statNo": {"type": "string"},
                    "subStatNo1": {"type": "string"},
                    "subStatNo2": {"type": "string"},
                    "procedure": {"type": "string"},
                    "value": {"type": "number"},
                    "goodsMark1": {"type": "string"},
                    "goodsMark2": {"type": "string"},
                    "goodsMark3": {"type": "string"},
                    "goodsMark4": {"type": "string"},
                    "goodsMark5": {"type": "string"},
                    "goodsMark6": {"type": "string"},
                    "contents": {"type": "string"},
                    "copies": {"type": "integer", "minimum": 1},
                    "netWeight": {"type": "number", "minimum": 0},
                    "sourceCountryCode": {"type": "string"},
                    "otherUnit": {"type": "string"},
                    "otherQuantity": {"type": "number", "minimum": 0}
                }
            }
        }
    }
}

ADDRESS_SCHEMA = {
    "type": "object",
    "oneOf": [
        {"required": ["name", "city", "country"]},
        {"required": ["quickId"]}
    ],
    "properties": {
        "quickId": {"type": "string"},
        "orgNo": {"type": "string"},
        "vatNo": {"type": "string"},
        "name": {"type": "string"},
        "address1": {"type": "string"},
        "address2": {"type": "string"},
        "zipcode": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "country": {"type": "string"},
        "contact": {"type": "string"},
        "phone": {"type": "string"},
        "fax": {"type": "string"},
        "email": {"type": "string"},
        "mobile": {"type": "string"},
        "doorCode": {"type": "string"},
        "serviceType": {"type": "string"},
        "serviceCode": {"type": "string"},
        "openingHours": {"type": "string"}
    },
}

AGENT_ITEM_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "city", "countryCode"],
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "address1": {"type": ["string", "null"]},
        "address2": {"type": ["string", "null"]},
        "zipcode": {"type": ["string", "null"]},
        "city": {"type": "string"},
        "state": {"type": ["string", "null"]},
        "countryCode": {"type": "string"},
        "contact": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "fax": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]},
        "sms": {"type": ["string", "null"]},
        "serviceType": {"type": ["string", "null"]},
        "serviceCode": {"type": ["string", "null"]},
        "openingHours": {"type": ["string", "null"]},
    },
}

AGENTS_SCHEMA = {
    "type": "array",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "items": AGENT_ITEM_SCHEMA,
}

PARTNER_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id"],
        "properties": {
            "id": {"type": "string"},
            "agentNo": {"type": "string"},
            "custNo": {"type": "string"},
            "custNoIssuerCode": {"type": "string"},
            "palletRegNo": {"type": "string"},
            "ediAddress": {"type": "string"},
            "senderId": {"type": "string"},
            "bookingId": {"type": "string"},
            "bookingOffice": {"type": "string"},
            "bookingEmail": {"type": "string"},
            "sourceCode": {"type": "string"},
            "ediUserId": {"type": "string"},
            "ediPassword": {"type": "string"},
            "ediKey": {"type": "string"},
            "externalIdentifier": {"type": "string"}
        }
    }
}

PARCELS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["copies"],
        "properties": {
            "valuePerParcel": {"type": "boolean"},
            "copies": {"type": "integer", "minimum": 1},
            "marking": {"type": "string"},
            "packageCode": {"type": "string"},
            "packageText": {"type": "string"},
            "weight": {"type": "number", "minimum": 0},
            "volume": {"type": "number", "minimum": 0},
            "length": {"type": "number", "minimum": 0},
            "width": {"type": "number", "minimum": 0},
            "height": {"type": "number", "minimum": 0},
            "loadingMeters": {"type": "number", "minimum": 0},
            "itemNo": {"type": "string"},
            "contents": {"type": "string"},
            "reference": {"type": "string"},
            "customLabelText1": {"type": "string"},
            "customLabelText2": {"type": "string"},
            "customLabelText3": {"type": "string"},
            "customLabelText4": {"type": "string"},
            "customLabelText5": {"type": "string"},
            "customLabelText6": {"type": "string"},
            "dangerousGoods": {
                "type": "object",
                "properties": {
                    "unCode": {"type": "string"},
                    "hazardCode": {"type": "string"},
                    "packageCode": {"type": "string"},
                    "packageType": {"type": "string"},
                    "description": {"type": "string"},
                    "adrClass": {"type": "string"},
                    "mpCode": {"type": "string"},
                    "ems": {"type": "string"},
                    "note": {"type": "string"},
                    "netWeight": {"type": "number"},
                    "netVolume": {"type": "number"},
                    "trCode": {"type": "string"},
                    "flashPoint": {"type": "string"},
                    "limitedQuantities": {"type": "boolean"},
                    "separation": {"type": "string"}
                }
            },
            "articles": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "articleNo": {"type": "string"},
                        "count": {"type": "integer"},
                        "name": {"type": "string"},
                        "enot": {"type": "boolean"},
                        "price": {"type": "number", "minimum": 0},
                        "currencyCode": {"type": "string"},
                        "weight": {"type": "number", "minimum": 0},
                        "volume": {"type": "number", "minimum": 0},
                        "loadingMeters": {"type": "number", "minimum": 0},
                        "contents": {"type": "string"},
                        "marking": {"type": "string"},
                        "packageCode": {"type": "string"},
                        "customsStatNo": {"type": "string"},
                        "customsSubStatNo1": {"type": "string"},
                        "customsOtherUnit": {"type": "string"},
                        "customsOtherQuantity": {"type": "number", "minimum": 0},
                        "customsValue": {"type": "number", "minimum": 0},
                        "customsContents": {"type": "string"},
                        "customsNetWeight": {"type": "number", "minimum": 0},
                        "customsSourceCountryCode": {"type": "string"},
                        "dangerousGoods": {
                            "type": "object",
                            "properties": {
                                "unCode": {"type": "string"},
                                "hazardCode": {"type": "string"},
                                "packageCode": {"type": "string"},
                                "packageType": {"type": "string"},
                                "description": {"type": "string"},
                                "adrClass": {"type": "string"},
                                "mpCode": {"type": "string"},
                                "ems": {"type": "string"},
                                "note": {"type": "string"},
                                "netWeight": {"type": "number"},
                                "netVolume": {"type": "number"},
                                "trCode": {"type": "string"},
                                "flashPoint": {"type": "string"},
                                "limitedQuantities": {"type": "boolean"},
                                "separation": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }
}

SERVICE_SCHEMA = {
    "type": "object",
    "required": ["id"],
    "properties": {
        "id": {"type": "string"},
        "subId": {"type": "string"},
        "normalShipment": {"type": "boolean"},
        "returnShipment": {"type": "boolean"},
        "referenceAsBarcode": {"type": "boolean"},
        "nonDeliveryType": {"type": "string"},
        "valueAmount": {"type": "string"},
        "valueCurrencyCode": {"type": "string"},
        "paymentMethodType": {"type": "string"},
        "sortPos": {"type": "string"},
        "destinationLocation": {"type": "string"},
        "notifyCode1": {"type": "string"},
        "notifyCode2": {"type": "string"},
        "notifyCode3": {"type": "string"},
        "bookingId": {"type": "string"},
        "bookingOffice": {"type": "string"},
        "infoCode": {"type": "string"},
        "contractVersion": {"type": "string"},
        "terminal": {"type": "string"},
        "handOverCode": {"type": "string"},
        "externalIdentifier": {"type": "string"},
        "waybillInvoice": {"type": "integer", "minimum": 0},
        "waybillEurCertificate": {"type": "integer", "minimum": 0},
        "waybillExportNotification": {"type": "integer", "minimum": 0},
        "waybillUnits332": {"type": "integer", "minimum": 0},
        "waybillWeight332": {"type": "number", "minimum": 0},
        "waybillUnits334": {"type": "integer", "minimum": 0},
        "waybillWeight334": {"type": "number", "minimum": 0},
        "waybillUnits336": {"type": "integer", "minimum": 0},
        "waybillWeight336": {"type": "number", "minimum": 0},
        "waybillUnits342": {"type": "integer", "minimum": 0},
        "waybillWeight342": {"type": "number", "minimum": 0},
        "waybillCod": {"type": "integer", "minimum": 0},
        "waybillCod342": {"type": "integer", "minimum": 0},
        "waybillHomeDelivery342": {"type": "integer", "minimum": 0},
        "shipperLoadAndCount": {"type": "integer", "minimum": 0},
        "pickupBooking": {"type": "boolean"},
        "pickupDate": {"type": "string"},
        "pickupTimeFrom": {"type": "string"},
        "pickupTimeTo": {"type": "string"},
        "pickupText1": {"type": "string"},
        "pickupMisc": {"type": "string"},
        "addons": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id"],
                "properties": {
                    "id": {"type": "string"},
                    "amount": {"type": "number", "minimum": 0},
                    "account": {"type": "string"},
                    "accountType": {"type": "string"},
                    "bank": {"type": "string"},
                    "currencyCode": {"type": "string"},
                    "custNo": {"type": "string"},
                    "custNoIssuerCode": {"type": "string"},
                    "misc": {"type": "string"},
                    "miscType": {"type": "string"},
                    "contact": {"type": "string"},
                    "reference": {"type": "string"},
                    "referenceType": {"type": "string"},
                    "tempMin": {"type": "number"},
                    "tempMax": {"type": "number"},
                    "email": {"type": "string"},
                    "text1": {"type": "string"},
                    "text2": {"type": "string"},
                    "text3": {"type": "string"},
                    "text4": {"type": "string"},
                    "text5": {"type": "string"},
                    "text6": {"type": "string"},
                    "text7": {"type": "string"},
                    "text8": {"type": "string"},
                    "text9": {"type": "string"},
                    "text10": {"type": "string"},
                    "length": {"type": "number", "minimum": 0},
                    "width": {"type": "number", "minimum": 0},
                    "declarant": {"type": "string"},
                    "passengerFlight": {"type": "boolean"},
                    "cargoFlight": {"type": "boolean"},
                    "documentType": {"type": "string"}
                }
            }
        }
    }
}

EXTRAS_SCHEMA = {
    "type": "object",
    "properties": {
        "favorite": {"type": "string"},
        "profileGroup": {"type": "string"},
        "note": {"type": "string"},
        "test": {"type": "boolean"},
        "linkPrintKey": {"type": "string"},
        "orderNo": {"type": "string"},
        "mergeId": {"type": "string"},
        "freeText1": {"type": "string"},
        "freeText2": {"type": "string"},
        "freeText3": {"type": "string"},
        "freeText4": {"type": "string"},
        "senderReference": {"type": "string"},
        "receiverReference": {"type": "string"},
        "goodsDescription": {"type": "string"},
        "bulkId": {"type": "string"},
        "totalEurPallets": {"type": "integer", "minimum": 0},
        "totalHalfPallets": {"type": "integer", "minimum": 0},
        "totalQuarterPallets": {"type": "integer", "minimum": 0},
        "totalWeight": {"type": "number", "minimum": 0},
        "totalVolume": {"type": "number", "minimum": 0},
        "totalLoadingMeters": {"type": "number", "minimum": 0},
        "totalSortCode": {"type": "string"},
        "totalQuantity": {"type": "integer", "minimum": 0},
        "totalPieces": {"type": "integer", "minimum": 0},
        "totalPallets": {"type": "integer", "minimum": 0},
        "waybillFreeText1": {"type": "string"},
        "waybillFreeText2": {"type": "string"},
        "waybillFreeText3": {"type": "string"},
        "waybillFreeText4": {"type": "string"},
        "waybillFreeText5": {"type": "string"},
        "waybillSpecialAgreement": {"type": "string"},
        "waybillDocuments1": {"type": "string"},
        "waybillDocuments2": {"type": "string"},
        "waybillCondition": {"type": "string"},
        "termsCode": {"type": "string"},
        "termsLocation": {"type": "string"},
        "termsLocationIdentifier": {"type": "string"},
        "printSet": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "shipDate": {"type": "string", "format": "date-time"},
        "pickupTime": {"type": "string", "format": "date-time"},
        "deliveryDate": {"type": "string", "format": "date-time"},
        "deliveryTimeEarliest": {"type": "string", "format": "date-time"},
        "deliveryTimeLastest": {"type": "string", "format": "date-time"},
        "shipmentNo": {"type": "string"},
        "ediForward": {"type": "boolean"},
        "tplFormat": {"type": "boolean"},
        "pdfInsert": {"type": "string"},
        "deliveryInstruction": {"type": "string"},
        "customLabelText1": {"type": "string"},
        "customLabelText2": {"type": "string"},
        "customLabelText3": {"type": "string"},
        "customLabelText4": {"type": "string"},
        "customLabelText5": {"type": "string"},
        "customLabelText6": {"type": "string"},
        "options": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id"],
                "properties": {
                    "id": {"type": "string"},
                    "from": {"type": "string"},
                    "to": {"type": "string"},
                    "cc": {"type": "string"},
                    "bcc": {"type": "string"},
                    "errorTo": {"type": "string"},
                    "message": {"type": "string"},
                    "languageCode": {"type": "string"},
                    "mailTemplate": {"type": "string"},
                    "sendEmail": {"type": "boolean"}
                }
            }
        }
    }
}

PDF_CONFIG_SCHEMA = {
    "type": "object",
    "required": ["target1Media"],
    "properties": {
        "target1Media": {"type": "string"},
        "target1XOffset": {"type": "number"},
        "target1YOffset": {"type": "number"},
        "target2Media": {"type": "string"},
        "target2XOffset": {"type": "number"},
        "target2YOffset": {"type": "number"},
        "target3Media": {"type": "string"},
        "target3XOffset": {"type": "number"},
        "target3YOffset": {"type": "number"},
        "target4Media": {"type": "string"},
        "target4XOffset": {"type": "number"},
        "target4YOffset": {"type": "number"}
    }
}

REQUEST_SCHEMA = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "required": ["shipment", "pdfConfig"],
    "properties": {
        "shipment": {
            "allOf": [
                {
                    "type": "object",
                    "required": ["sender", "receiver", "service", "parcels"],
                    "properties": {
                        "sender": ADDRESS_SCHEMA,
                        "senderPartners": PARTNER_SCHEMA,
                        "dispatch": ADDRESS_SCHEMA,
                        "receiver": ADDRESS_SCHEMA,
                        "receiverPartners": PARTNER_SCHEMA,
                        "delivery": ADDRESS_SCHEMA,
                        "agent": ADDRESS_SCHEMA,
                        "returnPart": ADDRESS_SCHEMA,
                        "freightPayer": ADDRESS_SCHEMA,
                        "taxPayer": ADDRESS_SCHEMA,
                        "customsPayer": ADDRESS_SCHEMA,
                        "service": SERVICE_SCHEMA,
                        "parcels": PARCELS_SCHEMA,
                        "customsDeclaration": CUSTOMS_DECLARATION_SCHEMA
                    }
                },
                EXTRAS_SCHEMA
            ]

        },
        "pdfConfig": PDF_CONFIG_SCHEMA
    }
}

RESPONSE_SCHEMA = {
    "type": "array",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "items": {
        "type": "object",
        "required": ["href", "id"],
        "properties": {
            "href": {"type": "string"},
            "id": {"type": "string"},
            "status": {"type": "string"},
            "shipmentNo": {"type": "string"},
            "orderNo": {"type": "string"},
            "reference": {"type": "string"},
            "serviceId": {"type": "string"},
            "parcelCount": {"type": "number"},
            "sndName": {"type": "string"},
            "sndZipcode": {"type": "string"},
            "sndCity": {"type": "string"},
            "sndCountry": {"type": "string"},
            "rcvName": {"type": "string"},
            "rcvZipcode": {"type": "string"},
            "rcvCity": {"type": "string"},
            "rcvCountry": {"type": "string"},
            "created": {"type": "string", "format": "date-time"},
            "changed": {"type": "string", "format": "date-time"},
            "shipDate": {"type": "string", "format": "date-time"},
            "returnShipment": {"type": "boolean"},
            "normalShipment": {"type": "boolean"},
            "consolidated": {"type": "boolean"},
            "parcels": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "parcelNo": {"type": "string"},
                        "reference": {"type": "string"}
                    }
                }
            },
            "pdfs": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["href", "id"],
                    "properties": {
                        "href": {"type": "string"},
                        "id": {"type": "string"},
                        "description": {"type": "string"}
                    }
                }
            },
            "previousPdfs": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["href", "id"],
                    "properties": {
                        "href": {"type": "string"},
                        "id": {"type": "string"},
                        "description": {"type": "string"}
                    }
                }
            }
        }
    }
}

LOCATION_ADDRESS_SCHEMA = {
    "type": "object",
    "properties": {
        "address": {"type": ["string", "null"]},
        "municipality": {"type": ["string", "null"]},
        "postalCode": {"type": ["string", "null"]},
        "postalCodeName": {"type": ["string", "null"]},
        "streetName": {"type": ["string", "null"]},
        "streetNumber": {"type": ["string", "null"]},
    }
}

LOCATION_ADDRESS_NAME_SCHEMA = {
    "type": "object",
    "properties": {
        "en": LOCATION_ADDRESS_SCHEMA,
        "fi": LOCATION_ADDRESS_SCHEMA,
        "sv": LOCATION_ADDRESS_SCHEMA,
    },
}

LOCATION_NAME_SCHEMA = {
    "type": ["object", "null"],
    "properties": {
        "en": {"type": ["string", "null"]},
        "fi": {"type": ["string", "null"]},
        "sv": {"type": ["string", "null"]},
    }
}

LOCATION_OPENING_TIME_SCHEMA = {
    "type": "object",
    "properties": {
        "timeFrom": {"type": "string"},
        "timeFromWithPoint": {"type": "string"},
        "timeTo": {"type": "string"},
        "timeToWithPoint": {"type": "string"},
        "weekday": {"type": "string"},
    }
}

LOCATION_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "type": {"type": "string"},
        "locationName": LOCATION_NAME_SCHEMA,
        "publicName": LOCATION_NAME_SCHEMA,
        "labelName": LOCATION_NAME_SCHEMA,
        "additionalInfo": LOCATION_NAME_SCHEMA,
        "postalCode": {"type": ["string", "null"]},
        "postalCodeAreas": {"type": ["array", "null"]},
        "address": LOCATION_ADDRESS_NAME_SCHEMA,
        "countryCode": {"type": "string"},
        "location": {
            "type": "object",
            "properties": {
                "lat": {"type": "string"},
                "lon": {"type": "string"},
            },
        },
        "openingTimes": {
            "type": ["array", "null"],
            "items": LOCATION_OPENING_TIME_SCHEMA,
        },
        "wheelChairAccess": {"type": "boolean"},
        "dropOfTimeParcel": {"type": ["string", "null"]},
        "dropOfTimeLetters": {"type": ["string", "null"]},
        "dropOfTimeExpress": {"type": ["string", "null"]},
        "pupCode": {"type": ["string", "null"]},
        "routingServiceCode": {"type": ["string", "null"]},
        "postalOfficeType": {"type": ["string", "null"]},
        "availability": {"type": ["string", "null"]},
        "partnerType": {"type": ["string", "null"]},
        "category": {"type": ["string", "null"]},
        "emptyTime": {"type": ["string", "null"]},
        "letterClass": {"type": ["string", "null"]},
        "capacity": {"type": ["string", "null"]},
    },
}

LOCATIONS_SCHEMA = {
    "type": "array",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "items": LOCATION_SCHEMA,
}
