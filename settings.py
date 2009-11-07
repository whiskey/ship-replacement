# Django settings for eve project.
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Carsten Witzke', 'carsten@staticline.de'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'                               # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = PROJECT_ROOT + '/database.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''                                        # Not used with sqlite3.
DATABASE_PASSWORD = ''                                    # Not used with sqlite3.
DATABASE_HOST = ''                                        # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
if DEBUG == True:
    MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), './media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
if DEBUG == True:
    MEDIA_URL = './media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

    
# Make this unique, and don't share it with anybody.
SECRET_KEY = '2c67p=&s!+9=-0#n77pi9q$$is5)tzfi_%qp2+tij)7!d&7awa'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.csrf.middleware.CsrfMiddleware',
    'eve.middleware.StripWhitespaceMiddleware',
)

ROOT_URLCONF = 'eve.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT + '/templates'),
)

#A tuple of callables that are used to populate the context in RequestContext. These 
#callables take a request object as their argument and return a dictionary of items to 
#be merged into the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'eve.replacement',
)
