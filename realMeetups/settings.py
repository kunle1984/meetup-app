"""
Django settings for realMeetups project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import environs
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n=+&u*xw(3$6-#ep7g*%@+c55il7o-w4ufzyl10q+#bbwj#i2_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meetups', 
    'storages',
    'rest_framework',
    "corsheaders",
    'rest_framework.authtoken'
]
AUTH_USER_MODEL = 'meetups.myUser'
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realMeetups.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'realMeetups.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

"""DATABASES = {
    'default': {
         #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': '5LiuHuqMCPxKsXQZQSKO',
        'HOST': 'containers-us-west-17.railway.app',
        'PORT': '7405',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

env=environs.Env()
environs.Env.read_env()

# DATABASES={
# #'default': dj_database_url.parse('postgres://meetup_j0wd_user:uhzpWQPrSlJ6qhmQ8iyUZMUcV68Kwx8C@dpg-cfvobtt269v0ptmr9tg0-a.oregon-postgres.render.com/meetup_j0wd')


# 'default':dj_database_url.parse(env('DATABASE_URL'))

# }

# DATABASES = {
#     'default': {
#          #'ENGINE': 'django.db.backends.sqlite3',
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get('DB_HOST'),
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASS'),
    
#     }
# }


DATABASES = {
    'default':dj_database_url.parse(env('DATABASE_URL'))
 
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

#cors origin

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIR=[
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

MEDIA_ROOT=os.path.join(BASE_DIR, 'uploads')
MEDIA_URL='/files/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




email_host= 'smtp.risinghopegirlseducation.com'
email_port =465
email_use_ssl = True
email_host_user ='admin@risinghopegirlseducation.com'
email_host_password = 'myadmin_1234'

# To email: contact form
recipient_address='kunlefes089@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =  email_host
EMAIL_PORT =email_port
EMAIL_USE_SSL = email_use_ssl
EMAIL_HOST_USER =email_host_user
EMAIL_HOST_PASSWORD =email_host_password


#S3 bucket
AWS_QUERYSTRING_AUTH=False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID='AKIATRQH4QNYEK2554YU'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME='kunlemeetups'

# To email: contact form
RECIPIENT_ADDRESS=recipient_address


CORS_ALLOWED_ORIGINS = [
        'https://k-meetups-production.up.railway.app',
        "http://localhost:8000"
        
    ]

CSRF_TRUSTED_ORIGINS = ['https://k-meetups-production.up.railway.app']
CORS_ALLOW_CREDENTIALS=True