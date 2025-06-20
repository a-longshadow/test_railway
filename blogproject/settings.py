"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-u++x9#uzr+=eytgdv)u8^dn%wcxg35l%240xik&j&o#tzt$)*a')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Environment detection
ENVIRONMENT = config('ENVIRONMENT', default='development')

# ALLOWED_HOSTS configuration
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Add Railway domains
railway_public_domain = config('RAILWAY_PUBLIC_DOMAIN', default='')
railway_static_url = config('RAILWAY_STATIC_URL', default='')

if railway_public_domain:
    ALLOWED_HOSTS.append(railway_public_domain)

if railway_static_url:
    # Extract domain from Railway URL
    import re
    domain_match = re.search(r'https?://([^/]+)', railway_static_url)
    if domain_match:
        ALLOWED_HOSTS.append(domain_match.group(1))

# Also add common Railway domain patterns
railway_domains = [
    'postgres-production-a65db.up.railway.app',
    'testrailway-production-904f.up.railway.app',  # New Railway domain
    '*.up.railway.app',
    '*.railway.app'
]
ALLOWED_HOSTS.extend(railway_domains)

# CSRF Trusted Origins for production
CSRF_TRUSTED_ORIGINS = []
if ENVIRONMENT == 'production':
    if railway_public_domain:
        CSRF_TRUSTED_ORIGINS.append(f'https://{railway_public_domain}')
    if railway_static_url:
        CSRF_TRUSTED_ORIGINS.append(railway_static_url)
    # Add common Railway URLs
    CSRF_TRUSTED_ORIGINS.extend([
        'https://postgres-production-a65db.up.railway.app',
        'https://testrailway-production-904f.up.railway.app',  # New Railway domain
        'https://*.up.railway.app',
        'https://*.railway.app'
    ])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'crispy_forms',
    'crispy_bootstrap4',
    
    # Local apps
    'blog',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if ENVIRONMENT == 'production' or config('POSTGRES_LOCALLY', default=False, cast=bool):
    # Production database configuration using dj-database-url
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL', default='')
        )
    }
else:
    # Development database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='blogdb'),
            'USER': config('DB_USER', default='postgres'),
            'PASSWORD': config('DB_PASSWORD', default='password'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Static files configuration for Railway deployment
if ENVIRONMENT == 'production':
    # Production static files configuration
    STATIC_ROOT = '/app/staticfiles'
    STATICFILES_DIRS = []
    # Ensure the directory exists
    os.makedirs(STATIC_ROOT, exist_ok=True)
else:
    # Development static files configuration
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
    STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise configuration for serving static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login/Logout redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
