"""Use this for production"""

from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True

WSGI_APPLICATION = 'baldi.wsgi.prod.application'



