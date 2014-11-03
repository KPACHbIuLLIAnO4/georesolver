
from zope.interface import implements

from pysyge.pysyge import GeoLocator, MODE_BATCH, MODE_MEMORY
from resolver.geoservices import interfaces

class SxGeo:
    implements(interfaces.ILocationResolver)
    
    def setAddrFile(self, file_name):
        self._geodata = GeoLocator(file_name, MODE_BATCH | MODE_MEMORY)

    def resolveLocation(self, ip_addr):
        return self._geodata.get_location(ip_addr, detailed=True)

