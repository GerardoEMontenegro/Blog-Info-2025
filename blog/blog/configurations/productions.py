from .base import *




DEBUG = False

#TODO configurar dominio de produccion
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

#configurar db para produccion
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #'ENGINE': 'django.db.backends.postgresql',  
        #'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.getenv('DB_NAME'),

        # 'USER': os.getenv('DB_USER'),

        # 'PASSWORD': os.getenv('DB_PASSWORD'),

        # 'HOST': os.getenv('DB_HOST', 'localhost'),

        # 'PORT': os.getenv('DB_PORT', '5432'),  

    }
}
os.environ['DJANGO__PORT'] = '8080'
