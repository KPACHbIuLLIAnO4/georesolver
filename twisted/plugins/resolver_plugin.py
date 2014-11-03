
import ConfigParser

from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker

from resolver import resolver

class Options(usage.Options):
    
    optParameters = [
        ['config', None, None, "Application config"]
    ]

class ResolverServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    
    tapname = "resolver"
    description = "Resolves geo by ip address"
    options = Options
    
    def makeService(self, options):
        
        config = ConfigParser.RawConfigParser();
        config.read(options['config']);
        
        return resolver.makeService(config)

serviceMaker = ResolverServiceMaker()

