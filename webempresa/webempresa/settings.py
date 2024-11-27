"""
Django settings for webempresa project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-01#drwse*=fv2llkhhtj=ojb0rv#&#6lorm1##rt3al(-kgov&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
		"django.contrib.admin",
		"django.contrib.auth",
		"django.contrib.contenttypes",
		"django.contrib.sessions",
		"django.contrib.messages",
		"django.contrib.staticfiles",
		"core", # Aplicación de Django: core.
		'services.apps.ServicesConfig', # Aplicación de Django: services.
		'blog.apps.BlogConfig', # Aplicación de Django: blog.
		'social.apps.SocialConfig', # Aplicación de Django: social.
		'pages.apps.PagesConfig', # Aplicación de Django: pages.
		'ckeditor', # Aplicación de Django: ckeditor sirve para editar texto como si fuera un Word.
		'contact', # Aplicación de Django: contact.
]

MIDDLEWARE = [
		"django.middleware.security.SecurityMiddleware",
		"django.contrib.sessions.middleware.SessionMiddleware",
		"django.middleware.common.CommonMiddleware",
		"django.middleware.csrf.CsrfViewMiddleware",
		"django.contrib.auth.middleware.AuthenticationMiddleware",
		"django.contrib.messages.middleware.MessageMiddleware",
		"django.middleware.clickjacking.XFrameOptionsMiddleware",
		'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "webempresa.urls"

TEMPLATES = [
		{
				"BACKEND": "django.template.backends.django.DjangoTemplates",
				"DIRS": [],
				"APP_DIRS": True,
				"OPTIONS": {
						"context_processors": [
								"django.template.context_processors.debug",
								"django.template.context_processors.request",
								"django.contrib.auth.context_processors.auth",
								"django.contrib.messages.context_processors.messages",
								'social.processors.ctx_dict', # Procesador de contexto personalizado.
								'django.contrib.auth.context_processors.auth', # Procesador de contexto de autenticación.
						],
				},
		},
]

WSGI_APPLICATION = "webempresa.wsgi.app"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
		"default": {
				"ENGINE": "django.db.backends.sqlite3", # Motor de la base de datos
				"NAME": BASE_DIR / "db.sqlite3", # Ruta de la base de datos
		}
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
		{
				"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
		},
		{
				"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
		},
		{
				"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
		},
		{
				"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
		},
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Ckeditor
CKEDITOR_CONFIGS = {
	'default': {
				'toolbar': 'Custom',
				'toolbar_Custom': [
									['Bold', 'Italic', 'Underline'],
									['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
									 '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight',
									 'JustifyBlock'],

									['Link', 'Unlink']
								  ]
				}
			}



# Email settings: Looking to send emails in production? Check out our Email API/SMTP product!

'''
Esto sirve para el local, si se tiene el archivo email_settings.json
en la raíz del proyecto. Se ha ocultado por seguridad.
'''

EMAIL_SETTINGS_FILE = os.path.join(BASE_DIR, 'email_settings.json')

# Verifica si el archivo existe.
if os.path.exists(EMAIL_SETTINGS_FILE):
	with open(EMAIL_SETTINGS_FILE) as f:
			email_settings = json.load(f)

	EMAIL_HOST = email_settings['EMAIL_HOST']
	EMAIL_HOST_USER = email_settings['EMAIL_HOST_USER']
	EMAIL_HOST_PASSWORD = email_settings['EMAIL_HOST_PASSWORD']
	EMAIL_PORT = email_settings['EMAIL_PORT']

else:
	# En Vercel y Github Actions se han definido las variables de entorno.
	EMAIL_HOST = os.getenv('EMAIL_HOST')
	EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
	EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
	EMAIL_PORT = os.getenv('EMAIL_PORT')

# Verifica si todas las variables están definidas
if not all([EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT]):
    raise ValueError("Faltan variables de entorno necesarias para la configuración de correo")
