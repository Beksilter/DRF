from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_db',
        'USER': 'beksilter',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '54326'
    }
}