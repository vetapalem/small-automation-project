import logging #logging module
logger = logging.getLogger(__name__)# root
logger.setLevel(logging.DEBUG) #log level
file_handler = logging.FileHandler(r'..\sample_pro.log') #log file 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p') #log formate 
file_handler.setFormatter(formatter) #log file handler
logger.addHandler(file_handler) #log addhandler 
def login_er():

    return logger #return logger object
    # logger.debug('Debug message')
    # logger.info('Info message')
    # logger.warning('Warning message')
    # logger.error('Error message')
    # logger.critical('Critical message')
