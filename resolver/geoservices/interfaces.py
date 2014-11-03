
from zope.interface import Interface

class ILocationResolver(Interface):
    
    def setAddrFile(file_name):
        """
        sets address file
        """
        
    def resolveLocation(ip_addr):
        """
        resolves an ip address into a location
        """

class ILocationResolverFactory(Interface):
    
    def getLocationResolver(resolver_type):
        """
        returns a location resolver based on it's type
        """

