from .base_settings import *
from os import getenv

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['movies.areslab.win', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [getenv('CSRF_TRUSTED_ORIGINS')]
