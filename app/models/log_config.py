import logging
from data.app_config import LOG_FILE


def setup_logging(log_file=LOG_FILE):
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )