import os
import django_heroku

from .base import *


django_heroku.settings(locals())
SECRET_KEY = os.environ['SECRET_KEY']
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'