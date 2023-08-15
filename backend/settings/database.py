# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": DB_NAME,
    #     "USER": DB_USER,
    #     "PASSWORD": DB_PASSWORD,
    #     "HOST": DB_HOST,
    #     "PORT": DB_PORT,
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
