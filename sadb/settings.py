"""
Django settings for sadb project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*f*s=_hc=x@e2+200min%v6%z4p-rwhrv_h&yfw)(3(+#v63zp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'sadb.urls'

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

WSGI_APPLICATION = 'sadb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
X_FRAME_OPTIONS = 'SAMEORIGIN'


'''
CELERY settings
'''
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Asia/Shanghai'

"""
Simple UI settings
"""
SIMPLEUI_HOME_TITLE = 'Sadb资产与配置中心'
SIMPLEUI_HOME_INFO = True
SIMPLEUI_LOGO = '/static/admin/simpleui-x/img/logo.png'
SIMPLEUI_LOGIN_PARTICLES = True
SIMPLEUI_HOME_ICON = 'fa fa-user'
SIMPLEUI_DEFAULT_THEME = 'Simpleui-x.css'
SIMPLEUI_ANALYSIS = False         # 不提交分析
SIMPLEUI_STATIC_OFFLINE = True    # simpleui 是否以脱机模式加载静态资源
SIMPLEPRO_INFO = False # 不显示激活信息
SIMPLEPRO_CHART_DISPLAY = False      # 配置Simple Pro是否显示首页的图标，默认为True，显示图表，False不显示
SIMPLEUI_HOME_ACTION = True
# SIMPLEUI_DEFAULT_ICON = False   # 不使用默认图标
SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['项目管理', '扫描管理', '资产管理', '漏洞管理', '扫描引擎', '日志管理', '认证和授权'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'menus': [{
        'app': 'targetApp',
        'name': '项目管理',
        'icon': 'fab fa-battle-net',
        'models': [{
            'name': '项目管理',
            'url': 'targetApp/project/',
            'icon': 'fas fa-cookie-bite'
            }, {
            'name': '目标管理',
            'url': 'targetApp/target/',
            'icon': 'fas fa-glasses'
            }]
        },
        {
            'name': '扫描管理',
            'url': 'scans/scans/',
            'icon': 'fas fa-anchor'
        },
        {
            'name': '扫描引擎',
            'url': 'scanEngine/enginetype/',
            # 'icon': 'fas fa-anchor'
            'icon': 'fab fa-d-and-d'
        }, {
        'app': 'assets',
        'name': '资产管理',
        'icon': 'fas fa-feather',
        'models': [{
            'name': '子域名',
            'url': 'assets/subdomain/',
            'icon': 'fab fa-apple'
        },{
            'name': 'IP资产',
            'url': 'assets/ip/',
            'icon': 'fas fa-skull-crossbones'
        },{
            'name': 'C段情报',
            'url': 'assets/ipc/',
            'icon': 'fas fa-skull-crossbones'
        },{
            'name': '端口服务',
            'url': 'assets/port/',
            'icon': 'fab fa-affiliatetheme'
        },{
            'name': 'web应用',
            'url': 'assets/webapp/',
            'icon': 'fas fa-dove'
        }, {
            'name': '黑名单资产',
            'url': 'assets/blockassets/',
            'icon': 'fas fa-times-circle'
            }
        ]
    }, {
        'app': 'vulnerability',
        'name': '漏洞管理',
        'icon': 'fas fa-user-secret',
        'models': [
            {
            'name': '文件指纹',
            'url': 'assets/fileleak/',
            'icon': 'fas fa-cat'
            }, {
            'name': 'URL爬虫',
            'url': 'assets/crawlerurl/',
            'icon': 'fas fa-spider'
            }, {
            'name': '主动扫描',
            'url': 'assets/nuclei/',
            'icon': 'fas fa-dragon'
            }, {
            'name': '被动扫描',
            'url': 'assets/rad2xray/',
            'icon': 'fas fa-frog'
            }
        ]
        },{
        'app': 'log',
        'name': '日志管理',
        'icon': 'fab fa-btc',
        'models': [
            {
            'name': 'Celery监控',
            'url': 'http://127.0.0.1:5555/',
            'icon': 'fas fa-skiing'
            }]
        }
    ]
}
