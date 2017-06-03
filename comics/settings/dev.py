from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comics',
        'USER': 'comics',
        'PASSWORD': 'comics',
        'HOST': 'localhost'
    }
}

INSTALLED_APPS.append('django_extensions')
