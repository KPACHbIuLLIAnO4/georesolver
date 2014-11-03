
from zope.interface import implements

from resolver.geoservices import sxgeo, interfaces

class FactoryException(Exception):
    pass

class LocationResolverFactory:
    implements(interfaces.ILocationResolverFactory)
    
    def getLocationResolver(self, resolver_type):
        
        if resolver_type == 'sxgeo':
            return sxgeo.SxGeo()
        
        raise FactoryException('Wrong resolver type: ' + resolver_type)

