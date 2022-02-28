from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DATABASE")}'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localHost:5432/cargill"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class Swagger():
    swagger_config = {
    'APISPEC_SPEC': APISpec(
        title='Cargil API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/docs/'  # URI to access UI of API Doc
    }

class path():
    logging_path = f"{basedir}/logging/logger.log"
