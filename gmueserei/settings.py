"""
Django settings for gmueserei project.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8cd-j&jo=-#ecd1jjulp_s*7y$n4tad(0d_g)l=6@n^r8fg3rn'
# SECRET_KEY = os.environ.get('GMUESEREI_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", "False") == "True"
# DEBUG = True

ALLOWED_HOSTS = ['mini.gmueserei.ch', 'localhost',]


ADMINS = (
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'gmueserei',
    'juntagrico',
    'fontawesomefree',  # benötigt ab 1.6
    'import_export',  # benötigt ab 1.6
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic'
    # 'juntagrico_billing',
]

ROOT_URLCONF = 'gmueserei.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','gmueserei.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'gmueserei.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '465' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False') =='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False') =='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

###LOGIN_REDIRECT_URL = "/my/home" #gültig vor Version 1.6
LOGIN_REDIRECT_URL = "/"

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view' #neu in 1.6

# Default Django Storage API behavior - don't overwrite files with same name
MEDIA_ROOT = 'media'

MEMBER_STRING = "Genossenschafter:in"
MEMBERS_STRING = "Genossenschafter:innen"
ASSIGNMENT_STRING = "Arbeitseinsatz"
ASSIGNMENTS_STRING = "Arbeitseinsätze"
ORGANISATION_NAME = "Gmüeserei"
ORGANISATION_LONG_NAME = "Genossenschaft GMÜESEREI SISSACH"
ORGANISATION_ADDRESS = {"name":"Genossenschaft GMÜESEREI SISSACH", 
            "street" : "Ebenrainweg",
            "number" : "25f",
            "zip" : "4450",
            "city" : "Sissach",
            "phone" : "078 480 35 99",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {"PC" : " ",
            "IBAN" : "CH1408390035190010009",
            "BIC" : "ABSOCH22",
            "NAME" : "Alternative Bank Schweiz",
            "ESR" : "ESR Number"}
###INFO_EMAIL = "mini@gmueserei.ch" #gültig vor Version 1.6
CONTACTS = {
    "general": "mini@gmueserei.ch"
}
###SERVER_URL = "gmueserei.ch" #gültig vor Version 1.6
ORGANISATION_WEBSITE = {
    'name': "www.gmueserei.ch",
    'url': "https://www.gmueserei.ch"
}
BUSINESS_REGULATIONS = ""
BYLAWS = "https://www.gmueserei.ch/index.php?page=dokumente"
STYLES = {'static': ['gm/css/personal.css','gm/css/gmueserei.css']}
FAVICON = {'static': ['img/favicon.ico']}
FAQ_DOC = ""
EXTRA_SUB_INFO = ""
ACTIVITY_AREA_INFO = ""
SHARE_PRICE = "250"
PROMOTED_JOB_TYPES = []
PROMOTED_JOBS_AMOUNT = 2
DEPOT_LIST_GENERATION_DAYS = [0,2]	
BILLING = False
BUSINESS_YEAR_START = {"day":1, "month":1}
BUSINESS_YEAR_CANCELATION_MONTH = 9
IMAGES = {'status_100': '/static/juntagrico/img/status_100.png',
            'status_75': '/static/juntagrico/img/status_75.png',
            'status_50': '/static/juntagrico/img/status_50.png',
            'status_25': '/static/juntagrico/img/status_25.png',
            'status_0': '/static/juntagrico/img/status_0.png',
            'single_full': '/static/juntagrico/img/single_full.png',
            'single_empty': '/static/juntagrico/img/single_empty.png',
            'single_core': '/static/juntagrico/img/single_core.png',
            'core': '/static/juntagrico/img/core.png'
}
EMAILS = {
    'b_share': 'mails/bill_share.txt',
    'b_sub': 'mails/bill_sub.txt',
    'b_esub': 'mails/bill_extrasub.txt'
}
DEFAULT_MAILER = 'juntagrico.util.mailer.default.Mailer'
BATCH_MAILER = {
    'batch_size': 30,
    'wait_time': 65
}

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
BASE_FEE='50'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

REQUIRED_SHARES = 1
ALLOW_JOB_UNSUBSCRIBE = True
ENABLE_NOTIFICATIONS = []
DISABLE_NOTIFICATIONS = []

