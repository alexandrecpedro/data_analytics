import logging

# 1. CONSTANTS
# ANSI color codes
COLORS = {
    'DEBUG': '\033[94m',   # Blue
    'INFO': '\033[92m',    # Green
    'WARNING': '\033[93m', # Yellow
    'ERROR': '\033[91m',   # Red
    'CRITICAL': '\033[95m' # Magenta
}
RESET_COLOR = '\033[0m'  # Reset to default color
LOGGER_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# 2. CLASS
class ColorFormatter(logging.Formatter):
    """Custom formatter for colored log levels"""
    def format(self, record):
        log_color = COLORS.get(record.levelname, RESET_COLOR)
        record.levelname = f'{log_color}{record.levelname}{RESET_COLOR}'
        return super().format(record=record)

# 3. SET UP LOGGING
def setup_logger():
    logging.basicConfig(
        format=LOGGER_FORMAT,
        handlers=logging.StreamHandler(),
        level=logging.INFO)

    logger = logging.getLogger()
    stream_handler = logger.handlers[0]
    stream_handler.setFormatter(ColorFormatter(LOGGER_FORMAT))
    return logger