"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from project.configs.base import *

# Application definition
from project.configs.apps import *


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
from project.configs.database import *


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
from project.configs.security import *

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
from project.configs.i18n import *


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
from project.configs.static import *
