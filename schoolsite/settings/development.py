from .base import *

SECRET_KEY = "4%%y0$i=ki4hek1q-01ac7x%gk63ujjxo43&$rm^loz)rl(4bh"
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", ]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "../db.sqlite3"),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = [
    "/mnt/c/Users/tomek/Projects/Python/schoolsite/static",
]

# ckeditor
CKEDITOR_PATH = STATICFILES_DIRS[0] + "/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
