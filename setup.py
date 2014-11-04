
__author__ = 'KPACHbIuLLIAnO4'

import sys

try:
    import twisted
except ImportError:
    raise SystemExit("twisted not found.  Make sure you "
                     "have installed the Twisted core package.")

from distutils.core import setup

def refresh_plugin_cache():
    from twisted.plugin import IPlugin, getPlugins
    list(getPlugins(IPlugin))

if __name__ == '__main__':
    
    if sys.version_info[:2] >= (2, 4):
        extraMeta = dict(
            classifiers=[
                "Development Status :: 4 - Beta",
                "Environment :: No Input/Output (Daemon)",
                "Programming Language :: Python",
            ])
    else:
        extraMeta = {}

    setup(
        name="resolver",
        version='1',
        description="Resolves geo by ip address",
        author=__author__,
        author_email="KPACHbIuLLIAnO4@users.noreply.github.com",
        url="https://github.com/KPACHbIuLLIAnO4/georesolver",
        packages=[
            "resolver",
            "twisted.plugins",
        ],
        package_data={
            'twisted': ['plugins/resolver_plugin.py'],
        },
        **extraMeta)
    
    refresh_plugin_cache()
