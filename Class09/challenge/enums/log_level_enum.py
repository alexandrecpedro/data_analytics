import logging
from enum import Enum


class LogLevel(Enum):
    """
    Defines the available log levels, mapping them to the standard Python
    'logging' module integer values.
    """
    DEBUG = logging.DEBUG  # 10: Informações detalhadas, tipicamente de interesse apenas
    INFO = logging.INFO  # 20: Confirmação de que as coisas estão funcionando como esperado
    WARNING = logging.WARNING  # 30: Indicação de que algo inesperado aconteceu, ou indicação de problema no futuro
    ERROR = logging.ERROR  # 40: O software não conseguiu executar alguma função
    CRITICAL = logging.CRITICAL  # 50: Um erro grave, indicando que o programa pode não continuar

    # Adicionando um alias comum para o nível padrão (opcional)
    DEFAULT = logging.INFO