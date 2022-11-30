SmartShip Change Log
====================

2.0.0
-----

Released at 2022-11-30 14:55 +0300.

* Updated Posti service and additional service codes based on those found on Posti documentation.
* Remove services that were not found on the latest smartship documentation.


1.2.0
-----

Released at 2018-09-25 14:10 +0300.

* Add free text field to shipment


1.1.2
-----

Released at 2018-08-29 13:10 +0300.

* Fix README formatting so that it is valid ReST


1.1.1
-----

Released at 2018-08-29 12:55 +0300.

* First Open Source release.


1.1.0
-----

Released at 2018-05-17 15:15 +0300.

* Add Posti location service
* Fix UnboundLocalError on invalid shipment response
* Update attrs package requirement


1.0.0
-----

Released at 2017-11-08 14:55 +0200.

* Add option for custom pdf config to posti carrier

* Change default pdfConfig for the PDF printout

  * Change the default pdfConfig, so that the pdf would fill the
    entire page.  Set it to accept custom pdfConfig values from
    plugin's implementations in different projects.

* Make sure decimal data can be sent as JSON

  * Require the simplejson library for requests to add Decimal
    serialization support.


0.2.0
-----

Released at 2017-04-24 16:30 +0300.


0.1.0
-----

Released at 2017-04-24 16:30 +0300.
