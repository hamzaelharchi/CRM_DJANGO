

from pathlib import Path
import os
#import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.

'''
env=environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
'''
DEBUG=True
#SECRET_KEY=os.environ.get('SECRET_KEY')

SECRET_KEY='fcsdfsd'
#DEBUG=env('DEBUG')
#SECRET_KEY=env('SECRET_KEY')
#DEBUG=os.environ.get('DEBUG')

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production


#ALLOWED_HOSTS = os.environ.get(list('ALLOWED_HOSTS'))

ALLOWED_HOSTS=['*']
# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'Dashboard.apps.DashboardConfig',
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    "whitenoise.runserver_nostatic",

    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",

]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



ROOT_URLCONF = 'Django-CRM.urls'
 
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

WSGI_APPLICATION = 'Django-CRM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

'''



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CRM_DJANGO',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'db',
        'PORT': 5432,
    }
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = "static_root"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL ='account.User'


LOGIN_REDIRECT_URL="/shop/products/"
SIGNUP_REDIRECT_URL="/shop/"

LOGOUT_REDIRECT_URL="/"

LOGIN_URL='/login'

APPEND_SLASH=False

#DEFAULT_AUTO_FIELD = 'django.db.models.UUIDField'

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST") 
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") 
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") 
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get("EMAIL_PORT") 
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")