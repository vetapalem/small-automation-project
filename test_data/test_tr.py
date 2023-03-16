import logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('pytest.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
def test_example():
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
