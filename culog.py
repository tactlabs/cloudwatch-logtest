import logging
import time


def info(*args):

    content = ' ' + str(time.asctime(time.localtime())) + ': '

    for arg in args:
        content +=  str(arg) + ' '
    
    logging.info(content)


def error(*args):

    content = ' ' + str(time.asctime(time.localtime())) + ': '

    for arg in args:
        content +=  str(arg) + ' '
    
    logging.error(content)