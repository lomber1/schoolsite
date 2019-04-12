from .base import *

SECRET_KEY = '4%%y0$i=ki4hek1q-01ac7x%gk63ujjxo43&$rm^loz)rl(4bh'
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "schoolsitelocal",
        "USER": "tomasz",
        "PASSWORD": "96530",
        "HOST": "localhost",
        "PORT": "5433",
    }
}
