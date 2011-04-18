from os.path import join, dirname


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(dirname(dirname(__file__)),'var','data.db')
    }
}

MEDIA_ROOT = join(dirname(dirname(__file__)), 'var', 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
SECRET_KEY = '-i-da7eh#8tp8w2s$d9@i8-3k2rj325m111mtph2fib_(#a8ak'

MIDDLEWARE_CLASSES = (
    'proxiedssl.middleware.ProxiedSslWsgiMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'proxiedssl.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
)
