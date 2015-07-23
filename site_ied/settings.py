# -*- coding: utf-8 -*-

import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for site_ied project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7-s$$*2al-!dqt-+&@r%x@esebpl5l&^b%l3=o(vj37q94oqxz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'site_ied.urls'

WSGI_APPLICATION = 'site_ied.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Etc/UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/static_tel/'

STATIC_ROOT = os.path.join(BASE_DIR, '../static').replace('\\', '/')
MEDIA_ROOT = os.path.join(BASE_DIR, '../static_tel').replace('\\', '/')

SITE_ID = 1


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),

        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.request",
                "sekizai.context_processors.sekizai",

                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
            ],
            'loaders': [
                 'django.template.loaders.filesystem.Loader',
                # important! place right before django.template.loaders.app_directories.Loader
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # important! place right before django.contrib.staticfiles.finders.AppDirectoriesFinder
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

INSTALLED_APPS = (
    'site_ied_plugins',
    'django_extensions',
    'djangocms_admin_style',
    'django_apogee',
    'duck_inscription',

    'mailrobot',
    'duck_utils',
    #  probleme migration
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',

    # 'aldryn_apphooks_config',
    # 'aldryn_boilerplates',
    # 'aldryn_categories',
    # 'aldryn_newsblog',
    # 'aldryn_people',
    # 'aldryn_reversion',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'filer',
    'parler',
    'reversion',
    'sortedm2m',
    'taggit',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cmsplugin_tabs',
    # 'aldryn_bootstrap3',
)

LANGUAGES = (
    ## Customize this
    ('fr', gettext('fr')),
    ('', gettext('')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': '',
            'hide_untranslated': False,
            'name': gettext(''),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('site_ied/fullwidth.html', 'Page'),
    ('site_ied/sidebar_left.html', 'Page avec Sidebar à Gauche'),
    ('site_ied/sidebar_right.html', 'Page avec sidebar à Droite'),
    ('site_ied/tpl_home.html', 'tpl_home'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}


MIGRATION_MODULES = {
    'aldryn_people': 'aldryn_people.migrations',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    # 'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    # 'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    # 'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    # 'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    # 'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    # 'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django'
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

THUMBNAIL_HIGH_RESOLUTION = True

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        ['Undo', '-', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles', 'Blockquote'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'skin': 'office2013',
    # 'default': {
        # 'basicEntities': False,
        # 'entities': False,
        # 'htmlbase': False,
        # 'entities_latin': False,
        # 'entities_greek': False,
        # 'removeFormatTags': '',
        # 'removeFormatAttributes': '',
        # 'autoParagraph': False,
        # 'fullPage': True,
        # 'protectedSource': ['/{% load .* %}'],
        # 'contentsLanguage': 'fr',
        # "removePlugins": "stylesheetparser, htmlwriter",
        # 'allowedContent': True,
        # 'clipboard_defaultContentType': 'text',
        # 'fillEmptyBlocks': False,
        # 'forcePasteAsPlainText': True,
    # },
}

# Bug fixed: <mark> tag was escaped into &lt;mark&gt;
# Solution: Add the following
TEXT_HTML_SANITIZE = False
CENTRE_SECU = (('', '------'), ('SMEREP', 'SMEREP'), ('LMDE', 'LMDE'))
try:
    from . import local_settings
    from .local_settings import *

except ImportError:
    local_settings = object