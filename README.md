georesolver
===========

Simple asynchronous web server for resolving ip address into geo data using sypex geo database (https://sypexgeo.net).
Requires twisted and pysyge library to be installed.

How to install:

- python setup.py install

How to start:

- twistd resolver --config=./config/application.ini

How to use:

- curl http://localhost:8080/{IPv4_addr}
