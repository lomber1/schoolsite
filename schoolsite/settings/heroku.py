from .base import *

import os
import django_heroku
import dj_database_url


DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["*.herokuapp.com"]

DATABASES = {
    "default": {

    }
}

DATABASES["default"] = dj_database_url.config(conn_max_age=600, 
                                              ssl_require=True)

django_heroku.settings(locals())
