"""
Django settings for site do caco project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys

import simplejson as json


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    config = json.load(open(BASE_DIR+'/config.json')) # Variáveis necessárias
except Exception as inst:
    print("Erro ao abrir o arquivo de configurações config.json")
    print(type(inst))
    print(inst)
    # Como nem carregou configuração, podemos sair do programa
    sys.exit(1)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# URL Base, usado em todos os links absolutos do site
URL_BASE = config['URL_BASE']

DEBUG = config['DEBUG']

ALLOWED_HOSTS = config['ALLOWED_HOSTS']

SITE_ID = 1

ADMINS = config['ADMINS']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    # 3rd part apps
    'haystack',
    'ckeditor',
    'ckeditor_uploader',
    'import_export',
    'analytical',
    'bootstrap3',
    'django_forms_bootstrap',

    # Os apps internos
    'sitecaco',
    'busca',
    'banco_de_provas',
    'noticias',
    'loja',
    'institucional',
    'paginas',
    'ouvidoria',
    'fisl',
    'banco_de_livros',
    'membros',
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

ROOT_URLCONF = 'sitecaco.urls'

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

WSGI_APPLICATION = 'sitecaco.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators8
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

# DATABASES
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Here we have two options: sqlite3 for development and postgres for production
if config['DATABASE_NAME'] == 'db.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
elif config['DATABASE_NAME'] == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config['DATABASE_NAME'],
            'USER': config['DATABASE_USER'],
            'PASSWORD': config['DATABASE_PASS'],
            'HOST': config['DATABASE_HOST'],
            'PORT': config['DATABASE_PORT'],
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = config['LANGUAGE_CODE']
TIME_ZONE = config['TIME_ZONE']
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# Static Files Finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles');
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Media files (Uploaded ones)
#
MEDIA_URL = '/media/'
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')


# Email Console backend - Se for debug, usa o console...
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Configuração do email
EMAIL_HOST = str(config['EMAIL_HOST'])
EMAIL_PORT = int(config['EMAIL_PORT'])
EMAIL_USE_TLS = config['EMAIL_USE_TLS']
EMAIL_HOST_USER = str(config['EMAIL_HOST_USER'])
EMAIL_HOST_PASSWORD = str(config['EMAIL_HOST_PASSWORD'])

# Search Engine
# Apenas configurado para haystack SimpleEngine
# https://django-haystack.readthedocs.io
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


# Configuração antibot do google (recaptcha)
RECAPTCHA_SECRET = config['RECAPTCHA_SECRET']

# Configuração do google analytics
GOOGLE_ANALYTICS_PROPERTY_ID = config['ANALYTICS_ID']
GOOGLE_ANALYTICS_SITE_SPEED = True

# Configuração do WYSIWYG CKEDITOR
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "web/"
CKEDITOR_IMAGE_BACKEND = 'pillow'

# Importa o autoreload do código para uWSGI caso esteja em deploy
# Usar somente com uWSGI
if not DEBUG:
    import sitecaco.uwsgireload
