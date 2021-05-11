from os.path import join

from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES

from .base import BASE_DIR

LANGUAGE_CODE = "en"
TIME_ZONE = "Africa/Lagos"
USE_I18N = True
LOCALE_PATHS = (join(BASE_DIR, "locale"),)
USE_L10N = True
USE_TZ = True

# English default
LANGUAGES = DJANGO_LANGUAGES