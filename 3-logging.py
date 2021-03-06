# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import logging
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything


#    Execute in new python interpreter
#    import logging
#    logging.basicConfig(filename='example.log', level=logging.DEBUG)
#    logging.debug('This message should go to the log file')
#    logging.info('So should this')
#    logging.warning('And this, too')


import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
