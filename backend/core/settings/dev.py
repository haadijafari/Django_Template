from .base import *

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Root folders for collected static files and media files (via 'collectstatic')
STATIC_ROOT = BASE_DIR / "static_cdn"
MEDIA_ROOT = BASE_DIR / "media_cdn"

STATICFILES_DIRS = [
    # BASE_DIR / "apps/frontend/next/src",
    BASE_DIR / "static",
]

# reCaptcha
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

# Cros Origin Settings
CORS_ALLOWED_ORIGINS = [
    # 'http://localhost:3000',
    # 'http://127.0.0.1:3000',
]
