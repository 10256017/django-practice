"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# import os
import environ

env = environ.Env()
env.read_env()
root = environ.Path(__file__) - 2  # -2表示路徑取到往上兩層
# 目前位置路徑
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = root()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 加密驗證
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# 模式
DEBUG = env('DEBUG', default=False)
# DEBUG = True

# 允許哪個網域存取
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions', #避免發文者亂填發文人(posts)
    'django_filters', #抓Post_id過濾(comments?post_id=1)
    'django_cleanup',

    'posts',
    'categories',
    'comments',
    'users',
]
# 中間層(require進來和出去都會經過)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 資料庫設定檔
DATABASES = {
    'default': env.db_url()
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# 密碼驗證
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 語言
LANGUAGE_CODE = 'en-us'  # zh-hant 中文
# 時區
TIME_ZONE = 'Asia/Taipei'
# 多國語言
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# 靜態檔存放路徑
STATIC_URL = '/static/'

AUTH_USER_MODEL = 'users.User'

# 驗證、權限
REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    # ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'djangorestframework_camel_case.parser.CamelCaseFormParser',
    #     'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    #     'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ #驗證
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [ #權限
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [ #過濾
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'JSON_UNDERSCOREIZE': {
    #     'no_underscore_before_number': True,
    # },
}

# email驗證
EMAIL_URL = env.email_url()
vars().update(EMAIL_URL)

# 上傳照片
MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')
