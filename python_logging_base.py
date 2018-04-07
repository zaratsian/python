
# https://docs.python.org/3/library/logging.html

import logging

logging.basicConfig(level=logging.CRITICAL) # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger = logging.getLogger(__name__)

# (Optional) Create file handler
handler = logging.FileHandler('zprogram.log')
handler.setLevel(logging.INFO)

# (Optional) Create a logging format
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Log msgs
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
logger.exception('exception message')


#ZEND
