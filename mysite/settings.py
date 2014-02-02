DEBUG = True

ADMINS = (
    ('Omar Yesid Marino', 'omar@dirplace.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dirplace',
        'USER': 'root',
        'PASSWORD': 'omar52hjb',
        'HOST': '',
        'PORT': '',
    }
}

AUTH_PROFILE_MODULE = 'dirplace.UserProfile'

TIME_ZONE = 'Etc/GMT-5'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = 'W:/dirPlace/mediafiles'
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    "W:/dirPlace/templates/static",
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '9217(vbk2thlv*dh*+x^@7c(!lgsrcse)cx(zkpqjn+w752mlrqnek359'

TEMPLATE_DEBUG = DEBUG
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    "W:/dirPlace/templates"
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'dirplace',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'mptt',
    'djangoratings',
    'captcha',
    'qrcode',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'dirplace.UserProfile'

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dirplace@gmail.com'
EMAIL_HOST_PASSWORD = 'tool_tic'
EMAIL_PORT = 587
EMAIL_CUSTOMER_ATTENDANT = 'omar@dirplace.com'

DEFAULT_FROM_EMAIL = 'dirPlace <info@dirplace.com>'

DOMAINURL = "http://127.0.0.1/"
DOMAINURL_NO_SLASH = "http://127.0.0.1"

ANONYMOUS_USER_ID = -1

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/logout/'

USERENA_DEFAULT_PRIVACY='registered'
USERENA_SIGNIN_REDIRECT_URL='/'
USERENA_ACTIVATION_REQUIRED = True
USERENA_ACTIVATION_DAYS = 9
USERENA_ACTIVATION_NOTIFY = True
USERENA_ACTIVATION_NOTIFY_DAYS = 3
USERENA_ACTIVATED = "ALREADY_ACTIVATED"
USERENA_REMEMBER_ME_DAYS = "(gettext('a month'), 30))"
USERENA_FORBIDDEN_USERNAMES = "('signup', 'signout', 'signin', 'activate', 'me', 'password')"
USERENA_MUGSHOT_GRAVATAR = False
USERENA_MUGSHOT_GRAVATAR_SECURE = False
USERENA_MUGSHOT_DEFAULT = "identicon"
USERENA_MUGSHOT_SIZE = 85
USERENA_MUGSHOT_PATH = "userPictures/"
USERENA_USE_HTTPS = False
USERENA_PROFILE_DETAIL_TEMPLATE = "userena/profile_detail.html"
USERENA_DISABLE_PROFILE_LIST = False
USERENA_USE_MESSAGES = True
USERENA_LANGUAGE_FIELD = 'language'
USERENA_WITHOUT_USERNAMES = True
USERENA_HIDE_EMAIL = True

MAX_UPLOAD_SIZE = '31457280'

RATINGS_VOTES_PER_IP = 1

CAPTCHA_NOISE_FUNCTIONS = None
CAPTCHA_FOREGROUND_COLOR = '#FF0000'
CAPTCHA_LETTER_ROTATION = None
CAPTCHA_FONT_SIZE = 27
CAPTCHA_FILTER_FUNCTIONS = ('captcha.helpers.post_smooth',)
CAPTCHA_LENGTH = 3