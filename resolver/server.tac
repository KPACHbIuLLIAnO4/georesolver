
from twisted.application import internet, service
from geoservice import factories

import resolver

geo_resolver_type = 'sxgeo';
geo_file          = 'SxGeoCity.dat'

port = 8080

factory = factories.LocationResolverFactory();

resolver_engine = factory.getLocationResolver(geo_resolver_type);
resolver_engine.setAddrFile(geo_file);

application = service.Application("Geo resolver")

# attach the service to its parent application
service = resolver.ResolverService(port, resolver_engine)
service.setServiceParent(application)

