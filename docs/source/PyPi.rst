Overview
========
This module provides an easy to use Python wrapper for the RadarIQ-M1 sensor (https://radariq.io/products/radariq-m1) which works
for both Python 2 & 3. This SDK has been tested with Windows, OSX, Raspberry Pi and Linux.

The RadarIQ-M1 sensor is an easy-to-use radar sensor for detecting objects and measuring distance and speed.
All the difficult parts of working with radar are done by the sensor and a simple API and SDK provide an easy
path to integration.

- Project Homepage: https://github.com/radariq/python-sdk
- Download Page: https://pypi.python.org/pypi/radariq

The RadarIQ Python SDK is released under the MIT software license, see LICENSE (https://github.com/radariq/python-sdk/LICENCE) for more details.


Documentation
=============
See https://radariq-python.readthedocs.io


Requirements
============
- Python 2 or 3
- A RadarIQ-M1 Sensor (https://radariq.io/products/radariq-m1)

Installation
============

Install the RadarIQ SDK using pip

    pip install radariq

The SDK can be used from Python scripts

    from radariq import RadarIQ

Usage
======

    from radariq import RadarIQ, MODE_POINT_CLOUD

    riq = RadarIQ()
    riq.set_mode(MODE_POINT_CLOUD)
    riq.set_units('m', 'm/s')
    riq.set_frame_rate(5)
    riq.set_distance_filter(0, 10)
    riq.set_angle_filter(-45, 45)
    riq.start()

    for row in riq.get_data():
        print(row)


Examples
========
Examples are in the directory examples: https://github.com/radariq/python-sdk/blob/master/examples


Other pages
===========

- Home Page: https://radariq.io
- Downloads: https://radariq.io
- GitHub: https://github.com/radariq
- Forum: https://forum.radariq.io
- Youtube channel: https://youtube.com/radariq
- Facebook page: https://facebook.com/radarIQsensing