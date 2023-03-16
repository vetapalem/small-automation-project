import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'D:\testing_pro1\project_level\sample_project\logs\sample_pro.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
def login_er():

    return logger
    # logger.debug('Debug message')
    # logger.info('Info message')
    # logger.warning('Warning message')
    # logger.error('Error message')
    # logger.critical('Critical message')