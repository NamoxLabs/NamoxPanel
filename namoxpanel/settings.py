"""
Django settings for namoxpanel project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from __future__ import unicode_literals

import django
import ast
import os
import os.path

import dj_database_url
import dj_email_url
from django.contrib.messages import constants as messages
import django_cache_url

name = "Namox Panel"

DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'True'))
SITE_ID = 1
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
ROOT_URLCONF = 'namoxpanel.urls'
WSGI_APPLICATION = 'namoxpanel.wsgi.application'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ofl@ud7f@se#r8f*5a2*%zip(d@04za43as73g(yix8pv7=sw4'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-bundle.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [
            r'.+\.hot-update\.js',
            r'.+\.map']}}

LOGOUT_ON_PASSWORD_CHANGE = False

ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
SEARCHBOX_URL = os.environ.get('SEARCHBOX_URL')
BONSAI_URL = os.environ.get('BONSAI_URL')

ES_URL = ELASTICSEARCH_URL or SEARCHBOX_URL or BONSAI_URL or ''
if ES_URL:
    SEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'namoxpanel.search.backends.elasticsearch2',
            'URLS': [ES_URL],
            'INDEX': os.environ.get('ELASTICSEARCH_INDEX_NAME', 'storefront'),
            'TIMEOUT': 5,
            'AUTO_UPDATE': True},
        'dashboard': {
            'BACKEND': 'namoxpanel.search.backends.dashboard',
            'URLS': [ES_URL],
            'INDEX': os.environ.get('ELASTICSEARCH_INDEX_NAME', 'storefront'),
            'TIMEOUT': 5,
            'AUTO_UPDATE': False}
    }
else:
    SEARCH_BACKENDS = {}

#GRAPHENE = {
#    'MIDDLEWARE': [
#        'graphene_django.debug.DjangoDebugMiddleware'
#    ],
#    'SCHEMA': 'namoxpanel.graphql.api.schema',
#    'SCHEMA_OUTPUT': os.path.join(
#        PROJECT_ROOT, 'namoxpanel', 'static', 'schema.json')
#}

SITE_SETTINGS_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'namoxpanel.core',
    'namoxpanel.apps',
    'namoxpanel.dashboard',
    'namoxpanel.registration',
    'namoxpanel.search',
    'namoxpanel.userprofile',

    # External apps
    'versatileimagefield',
    'babeldjango',
    'django_prices',
    'django_prices_openexchangerates',
    'emailit',
    'graphene_django',
    'mptt',
    'materializecssform',
    'webpack_loader',
    'django_countries',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'namoxpanel': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

AUTH_USER_MODEL = 'userprofile.User'

LOGIN_URL = '/account/login/'

DEFAULT_COUNTRY = 'MX'
DEFAULT_CURRENCY = 'MXN'
AVAILABLE_CURRENCIES = [DEFAULT_CURRENCY]

OPENEXCHANGERATES_API_KEY = os.environ.get('OPENEXCHANGERATES_API_KEY')
ACCOUNT_ACTIVATION_DAYS = 3

#Original
LOGIN_REDIRECT_URL = 'home'

GOOGLE_ANALYTICS_TRACKING_ID = os.environ.get('GOOGLE_ANALYTICS_TRACKING_ID')

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware'
)

if django.VERSION < (1, 11):
    MIDDLEWARE_CLASSES = MIDDLEWARE

if (2,) <= django.VERSION < (2, 1):
    from django.utils import deprecation
    # Anything to make mptt.templatetags.mptt_admin importable
    deprecation.RemovedInDjango20Warning = deprecation.RemovedInDjango21Warning

elif django.VERSION >= (2,):
    from django.utils import deprecation
    # Anything to make mptt.templatetags.mptt_admin importable
deprecation.RemovedInDjango20Warning = deprecation.RemovedInDjango30Warning

ROOT_URLCONF = 'namoxpanel.urls'

context_processors = [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]

#loaders = [
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
    # TODO: this one is slow, but for now need for mptt?
#    'django.template.loaders.eggs.Loader']

#if not DEBUG:
#    loaders = [('django.template.loaders.cached.Loader', loaders)]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': context_processors,
        'string_if_invalid': '<< MISSING VARIABLE "%s" >>' if DEBUG else ''}}]

WSGI_APPLICATION = 'namoxpanel.wsgi.application'
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split()
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

CACHES = {'default': django_cache_url.config()}

if os.environ.get('REDIS_URL'):
    CACHES['default'] = {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL')}

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://namoxpanel:namoxpanel@localhost:5432/namoxpanel',
        conn_max_age=600)
}

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

TIME_ZONE = 'America/Monterrey'
LANGUAGE_CODE = 'es'
LOCALE_PATHS = [os.path.join(PROJECT_ROOT, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    ('assets', os.path.join(PROJECT_ROOT, 'namoxpanel', 'static', 'assets')),
    ('images', os.path.join(PROJECT_ROOT, 'namoxpanel', 'static', 'images')),
    ('dashboard', os.path.join(PROJECT_ROOT, 'namoxpanel', 'static', 'dashboard'))
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]
