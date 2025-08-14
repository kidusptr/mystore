from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yh6o%&jdl96xe+kc8p#1bm22xfy21%qqk-=v4o_ivesm8e^20-"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mystore3",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "strong#123",
    }
}

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
