from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jayfeather151$default',
        'USER': 'jayfeather151',
        'PASSWORD': '1KQFCoRNLfwqe29',
        'HOST': 'jayfeather151.mysql.pythonanywhere-services.com'
    }
}

LOG_DIR = '/home/jayfeather151/logs'

# Logging handlers

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
