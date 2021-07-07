"""Use this for development"""

from .base import *
import os
from dotenv import load_dotenv

load_dotenv()


ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True

WSGI_APPLICATION = 'app.wsgi.dev.application'
ASGI_APPLICATION = 'app.asgi.application'



