"""
Django settings for celebrityproject project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import urllib
import os
import django_heroku
import dj_database_url
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l43v2ea^2&9@6ovc!5p&^qzaemau&b)k3#%i+s80!2b$x&pyuv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

AUTHENTICATION_BACKENDS = [


    'django.contrib.auth.backends.ModelBackend',


    'allauth.account.auth_backends.AuthenticationBackend',


]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth.socialaccount.providers.google',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'celebrityapp',
    'pagedown',
     'storages',
   ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'celebrityproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'celebrityproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')]

MEDIA_ROOT = os.path.join(BASE_DIR,'images')
MEDIA_URL = '/images/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SITE_ID = 1



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



#LINODE_BUCKET = 'destinypiz'
#LINODE_BUCKET_REGION = 'us-southeast-1'
#LINODE_BUCKET_ACCESS_KEY = 'R9TRJZRWXE7U0I37AR63'
#LINODE_BUCKET_SECRET_KEY = 'cfakTgBZouS2CXEFEqpY0yMuj1lAkBHuCCme5Xzg'
#AWS_S3_ENDPOINT_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'
#AWS_S3_REGION_NAME = LINODE_BUCKET_REGION
#AWS_S3_USE_SSL = True

"""
AWS_ACCESS_KEY_ID = 'AKIA2JYJCMVLUM5SS37O'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'destinypiz'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl':'max-age=86400'}
AWS_DEFAULT_ACL = 'None'
#AWS_S3_FILE_OVERWRITE = False
AWS_LOCATION = 'static'
"""
#STATICFILES_DIRS = [
  #  os.path.join(BASE_DIR,'static'),  ]

#STATIC_URL = F'https://{AWS_S3_CUSTOM_DOMAIN}/'

#STATIC_ROOT = F'https://{AWS_S3_CUSTOM_DOMAIN }/{AWS_LOCATION}/'
#



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =  587
EMAIL_USE_TLS = 'True'
EMAIL_HOST_USER = 'nwekelesley9@gmail.com'
EMAIL_HOST_PASSWORD = 'dymmugilboxripcz'
#SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


ACCOUNT_EMAIL_REQUIRED=True
#LOGIN_REDIRECT_URL = 'https://itzdestinypiz.herokuapp.com/accounts/login/'
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_EMAIL_VERIFICATION="mandatory"

ACCOUNT_ADAPTER = 'celebrityaphttps://itzdestinypiz.herokuapp.com/p.views.CustomAllauthAdapter'
BASE_URL = 'https://itzdestinypiz.herokuapp.com/'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True