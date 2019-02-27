"""
Django settings for aixianfeng project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1e46(kudug0(k=x0%)*@45re#gd=u=eh5fe%=r*0$%(7^l0(6+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'users.apps.UsersConfig',
	'App',
	'debug_toolbar',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'middleware.mymiddleware.LoginMiddleWare',
]

INTERNAL_IPS = ('127.0.0.1',)
ROOT_URLCONF = 'aixianfeng.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
			],
		},
	},
]

WSGI_APPLICATION = 'aixianfeng.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'aixianfeng',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '127.0.0.1',
		'PORT': '3306',

	}
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT=os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/static/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads')

EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.163.com'  # smtp.163.com smtp.qq.com
EMAIL_PORT = 25
EMAIL_HOST_USER = 'studenttest@163.com'  # 你的邮箱帐号
EMAIL_HOST_PASSWORD = 'studenttest1'  # 授权码密码
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.versions.VersionsPanel',
	'debug_toolbar.panels.timer.TimerPanel',
	'debug_toolbar.panels.settings.SettingsPanel',
	'debug_toolbar.panels.headers.HeadersPanel',
	'debug_toolbar.panels.request.RequestPanel',
	'debug_toolbar.panels.sql.SQLPanel',
	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	'debug_toolbar.panels.templates.TemplatesPanel',
	'debug_toolbar.panels.cache.CachePanel',
	'debug_toolbar.panels.signals.SignalsPanel',
	'debug_toolbar.panels.logging.LoggingPanel',
	'debug_toolbar.panels.redirects.RedirectsPanel',
]

# LOGGING = {
# 	'version': 1,
# 	'disable_existing_loggers': True,
# 	'formatters': {
# 		'standard': {
# 			'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
# 		# 日志格式
# 	},
# 	'filters': {
# 	},
# 	'handlers': {
# 		'mail_admins': {
# 			'level': 'ERROR',
# 			'class': 'django.utils.log.AdminEmailHandler',
# 			'include_html': True,
# 		},
# 		'default': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': 'log/all.log',  # 日志输出文件
# 			'maxBytes': 1024 * 1024 * 5,  # 文件大小
# 			'backupCount': 5,  # 备份份数
# 			'formatter': 'standard',  # 使用哪种formatters日志格式
# 		},
# 		'error': {
# 			'level': 'ERROR',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': 'log/error.log',
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		},
# 		'console': {
# 			'level': 'DEBUG',
# 			'class': 'logging.StreamHandler',
# 			'formatter': 'standard'
# 		},
# 		'request_handler': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': 'log/script.log',
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		},
# 		'scprits_handler': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': 'log/script.log',
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		}
# 	},
# 	'loggers': {
# 		'django': {
# 			'handlers': ['default', 'console'],
# 			'level': 'DEBUG',
# 			'propagate': False
# 		},
# 		'django.request': {
# 			'handlers': ['request_handler'],
# 			'level': 'DEBUG',
# 			'propagate': False,
# 		},
# 		'scripts': {
# 			'handlers': ['scprits_handler'],
# 			'level': 'INFO',
# 			'propagate': False
# 		},
# 		'App.views': {
# 			'handlers': ['default', 'error'],
# 			'level': 'DEBUG',
# 			'propagate': True
# 		},
# 		'users.views': {
# 			'handlers': ['default', 'error'],
# 			'level': 'DEBUG',
# 			'propagate': True
# 		},
# 	}
# }
