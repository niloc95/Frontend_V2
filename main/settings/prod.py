from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['frontend.co.za', '18.168.124.18' ]


#HTTPS SETTINGS
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

#HSTS SETTINGS
# SECURE_HSTS_SECONDS = 31536000 # 1 YEAR
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True