from os.path import join

from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR  # noqa

SWAG = True

INSTALLED_APPS += [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
]

MIDDLEWARE += [
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

STATIC_ROOT = join(BASE_DIR, 'static')

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

WAGTAIL_SITE_NAME = 'The Osher Encod3D'