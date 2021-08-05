import logging, os
if not os.path.exists('c:\log'):
    os.makedirs('c:\log')
logging.basicConfig(filename='c:\log\example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')