from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_db',
        'USER': 'beksilter',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432'
    }
}