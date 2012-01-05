Introduction
------------

This module provides a Django middleware class, 
``proxiedssl.middleware.ProxiedSslWsgiMiddleware``, that looks for one of two 
headers and sets the WSGI URL scheme to the value of the header. This allows a 
proxy server that handles SSL to notify the Django WSGI request handler that the 
end user is accessing the site through SSL.

Installation
------------

Add ``proxiedssl.middleware.ProxiedSslWsgiMiddleware`` to the 
``MIDDLEWARE_CLASSES`` tuple in your settings file. It would be best if it was 
first so that the ``is_secure`` method is accurate for the other middleware 
classes.

Requirements
------------

Django and you currently must be using the WSGI handler either through a WSGI 
server or through the FCGI server which is a wrapper around the WSGI server.

TODO
----

* Add a middleware class for the mod_python handler
* Add full unit tests
