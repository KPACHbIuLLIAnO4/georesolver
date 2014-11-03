georesolver
===========

Simple asynchronous web server for resolving ip address into geo data using sypex geo database (https://sypexgeo.net).
Requires twisted and pysyge library to be installed.

How to install:

- python setup.py install
- download file SxGeoCity.dat and put it into project root
- adjust config/application.ini if needed 

How to start:

- twistd resolver --config=./config/application.ini

How to use:

- curl http://localhost:8080/{IPv4_addr}
