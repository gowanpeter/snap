import logging

logging.basicConfig(filename='main_logger', filemode='w', level=logging.DEBUG, format='%(asctime)s %(module)s %(funcName)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

log = logging.getLogger(__name__)
log.debug('in snap.__init__.py')
