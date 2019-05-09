from .base import *
import django_heroku


django_heroku.settings(locals())

# ckeditor
CKEDITOR_PATH = STATICFILES_DIRS[0] + "/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
