import logging

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)

def errors():
    logging.basicConfig()

    logger = logging.getLogger()

    logger.critical('Your CRITICAL message')
    logger.error('Your ERROR message')
    logger.warning('Your WARNING message')
    logger.info('Your INFO message')
    logger.debug('Your DEBUG message')


def deb():
    import logging

    logging.basicConfig()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logger.critical('Your CRITICAL message')
    logger.error('Your ERROR message')
    logger.warning('Your WARNING message')
    logger.info('Your INFO message')
    logger.debug('Your DEBUG message')



def tim():
    import logging

    FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

    logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

    logger = logging.getLogger()

    logger.critical('Your CRITICAL message')
    logger.error('Your ERROR message')
    logger.warning('Your WARNING message')
    logger.info('Your INFO message')
    logger.debug('Your DEBUG message')
tim()