class ProxiedSslWsgiMiddleware(object):
    
    def process_request(self, request):
        print str(request.META)
        if 'HTTP_X_URL_SCHEME' in request.META:
            request.environ['wsgi.url_scheme'] = \
                request.META['HTTP_X_URL_SCHEME'].lower()
        elif 'HTTP_X_FORWARDED_PROTOCOL' in request.META:
            request.environ['wsgi.url_scheme'] = \
                request.META['HTTP_X_FORWARDED_PROTOCOL'].lower()
