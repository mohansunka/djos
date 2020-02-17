"""
Django settings for OnlineShop project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR=os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=mez2!!s646w63ho^#-0jk@da7sj^6&#fe5!axi&d_@647%vj0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'cart',
    'orders',
    'payment',
    'ckeditor',
    'ckeditor_uploader',
    'materialize',
    # 'materializecssform',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OnlineShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'OnlineShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djshop',
        'USER': 'postgres',
        'PASSWORD': 'post',
        'HOST':'127.0.0.1',
        'PORT':'5432'
    }
}


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
STATICFILES_DIRS=[
    STATIC_DIR,
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CART_SESSION_ID = 'cart'

# settings.py
# STRIPE_PUBLISHABLE_KEY = 'pk_test_uQJbDKJJ9hXcjGvZPWl3zgjE00xSAO4r70'
# STRIPE_SECRET_KEY = 'sk_test_GtEIL1grUwo489tR6bPmR5wS00AXKISK15'
# STRIPE_PUBLISHABLE_KEY= '<your test publishable key here>'
STRIPE_PUBLISHABLE_KEY= 'pk_test_JubC0XqvwVB0de3RC1vMZUmj00z1AldTk9'
# STRIPE_SECRET_KEY = '<your test secret key here>'
STRIPE_SECRET_KEY = 'sk_test_1wK0SKwyPrvLYUQI8OurpWiv00ku7UTGN9'


# # my_project/settings.py
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

# # my_project/settings.py
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join


# email backend
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'myfriendkhendelwal@gmail.com'
# EMAIL_HOST_PASSWORD = '**********'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# my email,sms,payment
# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIT_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_USER = 'mohansunki10@gmail.com'
EMAIL_HOST_PASSWORD = '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'

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "/media/uploads/"
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/uploads/')
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

LOGIN_REDIRECT_URL = 'shop:product_list'

LOGOUT_REDIRECT_URL = 'shop:product_list'

SITE_ID = 1
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
# }

import datetime

# JWT_AUTH ={
#     # "JWT_AUTH_HEADER_PREFIX" :'JWT',
#     # "JWT_EXPIRATION_DELTA":datetime.timedelta(seconds=300),
#
#     "JWT_AUTH_HEADER_PREFIX" :'jwt',
#     "JWT_EXPIRATION_DELTA":datetime.timedelta(seconds=120),
# }
