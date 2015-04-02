georesolver
===========

Simple asynchronous web server for resolving ip address into geo data using sypex geo database (https://sypexgeo.net).
Requires twisted and pysyge library to be installed.

Required:

- python
- virtualenv
- python-pip

How to install (in work dir):

- virtualenv .
- . ./bin/activate
- pip install twisted pysyge
- git clone https://github.com/KPACHbIuLLIAnO4/georesolver
- cd georesolver
- python setup.py build 
- python setup.py install
- (download file SxGeoCity.dat and put it into any accessible directory)

How to start (in work dir):

- . ./bin/activate
- twistd resolver --host localhost --port 8080 --file ./SxGeoCity.dat

How to bind on all interfaces:

- twistd resolver --host '' --port 8080 --file ./SxGeoCity.dat


How to use:

- curl http://localhost:8080/{IPv4_addr}
