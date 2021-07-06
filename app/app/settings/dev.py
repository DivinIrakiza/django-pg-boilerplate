"""Use this for development"""

from .base import *
import os
from dotenv import load_dotenv

load_dotenv()


ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True

WSGI_APPLICATION = 'baldi.wsgi.dev.application'
ASGI_APPLICATION = 'baldi.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('MONGODB_DBNAME'),
        'CLIENT': {
            'host': os.getenv('MONGO_LOCAL_URI'),
        }
    }
}

