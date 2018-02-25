#from local_conf import *

import os

class Logger(object):
    def __init__(self, name):
        self.name = name
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        print self.BASE_DIR

    def log(self, text):
        
        
        path = os.path.join(self.BASE_DIR, 'logs')
        log_file = open('%s/%s' % (path, "LOG") , 'a')
        log_file.write('\n ' + self.name +': ' + str(text))
        log_file.close()

