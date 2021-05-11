from .base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-6_*o0aavc&n4ac7srumb_h_p3ixxqozlce6a=xnc3s#m46l1t'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
