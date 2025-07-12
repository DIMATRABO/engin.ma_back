import logging
import sys

class Log:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Log, cls).__new__(cls)
        return cls._instance

    def __init__(self, debug=False, log_level=logging.DEBUG):
        if not hasattr(self, '_initialized'):  # Ensure __init__ is called only once
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(log_level)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

            self.is_debug = debug
            self.logger.debug("initialized logger")

            self._initialized = True  # Mark the instance as initialized

    def log(self, message, level=logging.DEBUG):
        self.logger.log(level, message)

    def debug(self, message):
        self.log(message, logging.DEBUG)

    def info(self, message):
        self.log(message, logging.INFO)

    def warning(self, message):
        self.log(message, logging.WARNING)

    def error(self, message):
        self.log(message, logging.ERROR)

    def critical(self, message):
        self.log(message, logging.CRITICAL)

    def exception(self, message):
        self.logger.exception(message)
