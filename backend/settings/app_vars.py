import os

from dotenv import load_dotenv

Use_Docker = False
# Use_Docker = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

if Use_Docker is False:
    load_dotenv()

    # Debug
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # Redis
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

    # CELERY settings
    CELERY_BROKER_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)
    CELERY_RESULT_BACKEND = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)

    # Secret_key
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv("SECRET_KEY")

else:
    # Debug
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = os.environ.get("DEBUG")

    FRONTEND_URL = os.environ.get("FRONTEND_URL")

    # Redis
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")

    # CELERY settings
    CELERY_BROKER_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)
    CELERY_RESULT_BACKEND = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)

    # Secret_key
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get("SECRET_KEY")
