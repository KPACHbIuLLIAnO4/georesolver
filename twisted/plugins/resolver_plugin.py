
from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker

from resolver import resolver

class Options(usage.Options):
    
    optParameters = [
        ['host',     'h', 'localhost', 'Local host for tcp socket'],
        ['port',     'p', 8080,        'Local port for tcp socket', int],
        ['resolver', 'r', 'sxgeo',     'Geo resolver. Only sxgeo supported'],
        ['file',     'f', None,        'File with geo data']
    ]
    
    def postOptions(self):
        if self['file'] is None:
            raise usage.UsageError, "No geo file defined"

class ResolverServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    
    tapname = "resolver"
    description = "Resolves geo by ip address"
    options = Options
    
    def makeService(self, options):
        
        return resolver.makeService(options)

serviceMaker = ResolverServiceMaker()

