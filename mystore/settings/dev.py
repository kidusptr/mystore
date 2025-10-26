import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl
from .common import *

load_dotenv()
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yh6o%&jdl96xe+kc8p#1bm22xfy21%qqk-=v4o_ivesm8e^20-"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Add these at the top of your settings.py


# Replace the DATABASES section of your settings.py with this

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "mystore_dev",
#         "USER": tmpPostgres.username,
#         "PASSWORD": tmpPostgres.password,
#         "HOST": tmpPostgres.hostname,
#         "PORT": 5432,
#         "OPTIONS": {
#             "sslmode": "require",  # Important for Neon
#             "options": "endpoint=ep-jolly-mode-a2cpci3s",
#         },
#     }
# }
MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mystore3",
        "HOST": "mysql",
        "USER": "root",
        "PASSWORD": "strong#123",
    }
}


CELERY_BROKER_URL = "redis://redis:6379/1"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

EMAIL_HOST = "smtp4dev"
EMAIL_PORT = 2525
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}
