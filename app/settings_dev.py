from settings_common import *
import os

# General
DEBUG = True
SECRET_KEY = 'SecretKeyForDevelopmentEnvironment'
SITE_NAME = 'Lexpage-devel'
SITE_DEMONYM = 'Lexpagiens'


# Static
MINIFY_JS = MINIFY_CSS = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Utilisation du backend PostgreSQL avec psycopg2
        'NAME': os.environ.get('DATABASE_NAME', 'postgre'),  
        'USER': os.environ.get('DATABASE_USER', 'luigitms'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'Adminpatroni2023/'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),      
    }
}


# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'lexpage',
    }
}


# Email & admin
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin.dev@fakemail.com'
ADMINS = (
    ('AdminDev', 'admin.dev@fakemail.com'),
)
MANAGERS = ADMINS


# Recaptcha
RECAPTCHA_PRIVATE_KEY = None
NOCAPTCHA = False  # Input field, enter "PASSED" in the captcha field to bypass captcha while testing.
os.environ['RECAPTCHA_TESTING'] = 'True'


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}


# Tests
SELENIUM_WEBDRIVER = os.environ.get('SELENIUM_WEBDRIVER', None)
RUN_NPM_TESTS = os.environ.get('RUN_NPM_TESTS', False)
