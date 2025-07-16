from .base import *
DEBUG = False


#TODO configurar domninio de produccion
ALLOWED_HOSTS = ['localhost', '127.0.0.1','mydmidomio-production.com']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#TODO configurar base de datos de produccion
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'), 
     }
 }

os.environ['DJANGO_PORT'] = '8080'