import os

from decouple import config
from datetime import timedelta

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [

    "http://localhost:4000",
]



# Application definition

INSTALLED_APPS = [
    "daphne",
     
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    'django_twilio',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME':     config('DB_NAME'),  
        'USER':     config('DB_USER'),  
        'PASSWORD': config('DB_PASSWORD'),  
        'HOST':     config('DB_HOST'),  
        'PORT':     config('DB_PORT'),  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
 
    }  
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/




STATIC_URL  = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'templates', 'static')

MEDIA_URL  = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'templates', 'media')


AUTH_USER_MODEL = 'app.User'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



######################### Djoser configuration ###########################
#######################################################################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
   
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

   
}

DOMAIN ="localhost:4000"
SITE_NAME ="Mon site frontend"



DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL'            : 'activate/{uid}/{token}',
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # 'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # 'PASSWORD_RESET_CONFIRM_RETYPE': True,
    # 'USERNAME_RESET_CONFIRM_RETYPE': True,
    # 'LOGOUT_ON_PASSWORD_CHANGE'    : True,
    # 'SET_PASSWORD_RETYPE'          : True,
    # 'USER_CREATE_PASSWORD_RETYPE'  : True,
    # 'SEND_CONFIRMATION_EMAIL'      : True,
    'SEND_ACTIVATION_EMAIL'        : True,
    

    
    'SERIALIZERS': {
        'user_create': 'app.controllers.User.serializers.UserCreateSerializer',
        'user'       : 'app.controllers.User.serializers.UserCreateSerializer',
        'user_delete': 'app.controllers.User.serializers.UserDeleteSerializer',
    }
      
}


EMAIL_BACKEND        = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST           = 'smtp.gmail.com'
EMAIL_PORT           =  587
EMAIL_HOST_USER      = 'oumarcisse.bfk@gmail.com'
EMAIL_HOST_PASSWORD  = 'xagogzvdptclxfui' 
EMAIL_USE_TLS        =  True
EMAIL_USE_SSL        =  False
DEFAULT_FROM_EMAIL   = 'Mon site web'


# Configuration de Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'



"""
    TWILIO_RECOVERY_CODE = WL2MUY8XUUZ9QCNYSPD2T7E7
"""
TWILIO_PHONE_NUMBER =  '+224628797137'
TWILIO_DEFAULT_CALLERID = '+224'

TWILIO_ACCOUNT_SID = 'AC4aae43ccbb15f6c465099088874cb4ba'
TWILIO_AUTH_TOKEN  = '68d484cb2eb54dcf46609c9009c96a78'

TWILIO_ACCOUNT_SID_TEST = 'AC1de3aba702536713a13ad1544b4f30fc'
TWILIO_AUTH_TOKEN_TEST  = 'a4499265554043662a2e849f941ca78f'