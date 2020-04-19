import logging
import datetime

def log_write(message, level = "debug"):
    logging.basicConfig(filename='./LOG/'+datetime.datetime.now().strftime("%Y-%m-%d")+'.log', format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG, filemode='a', datefmt='%Y-%m-%d %I:%M:%S %p')
    if level == "error":
        logging.error(message)
    elif level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    else:
        logging.debug(message)
