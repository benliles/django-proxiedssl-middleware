from logging import getLogger



log = getLogger('proxiedssl')

class ProxiedSslWsgiMiddleware(object):
    def process_request(self, request):
        if 'HTTP_X_URL_SCHEME' in request.META:
            log.debug('setting wsgi.url_scheme to %s' % 
                      (request.META['HTTP_X_URL_SCHEME'].lower(),))
            request.environ['wsgi.url_scheme'] = \
                request.META['HTTP_X_URL_SCHEME'].lower()
        elif 'HTTP_X_FORWARDED_PROTOCOL' in request.META:
            log.debug('setting wsgi.url_scheme to %s' % 
                      (request.META['HTTP_X_FORWARDED_PROTOCOL'].lower(),))
            request.environ['wsgi.url_scheme'] = \
                request.META['HTTP_X_FORWARDED_PROTOCOL'].lower()
        else:
            return
        log.debug('request.is_secure = %s' % (request.is_secure(),))
