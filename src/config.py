import logging
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')

    # Configuración de logging
    LOGGING_LEVEL = logging.DEBUG  # Puedes cambiar a INFO, WARNING, ERROR, etc.
    LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOGGING_FILE = 'api.log'  # Opcional: guardar logs en un archivo

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
}
