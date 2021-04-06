import decouple
from django.core.exceptions import ImproperlyConfigured

ENV_PRODUCTION = "production"
ENV_DEVELOPMENT = "development"

APPLICATION_ENVIRONMENT = decouple.config("DJANGO_ENV")

ENVIRONMENTS = (ENV_PRODUCTION, ENV_DEVELOPMENT)

if APPLICATION_ENVIRONMENT not in ENVIRONMENTS:
    raise ImproperlyConfigured("Invalid DJANGO_ENV setting")

if APPLICATION_ENVIRONMENT == ENV_DEVELOPMENT:
    from .development import *  # NOQA
elif APPLICATION_ENVIRONMENT == ENV_PRODUCTION:
    from .production import *  # NOQA
