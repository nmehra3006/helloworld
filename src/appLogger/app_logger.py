import logging
from configparser import ConfigParser
from logging.config import fileConfig


class AppLogger(object):
    __logger_instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if AppLogger.__logger_instance != None:
            return AppLogger.__logger_instance

        self.log_level = None
        self.log_file = None
        self.log_format = None
        self.log_path = None
        self.__loadLogConfig()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppLogger.__logger_instance == None:
            AppLogger.__logger_instance = AppLogger()
        return AppLogger.__logger_instance

    def __loadLogConfig(self):

        config = ConfigParser()
        config.read('logging.cfg')
        self.log_level = config['settings']['log_level']
        #self.log_format = config['settings']['log_format']
        self.log_format = "%(asctime)s {app} [%(thread)d] %(levelname)-5s %(name)s - %(message)s. [file=%(filename)s:%(lineno)d]"
        self.log_file = config['settings']['log_file']
        self.log_path = config['settings']['log_path'] + '/' + self.log_file
        print(self.log_path)
        #__log_date = config['settings']['log_datefmt']

        # fileConfig('logging_config.ini')
        if self.log_level == "DEBUG":
            logging.basicConfig(filename=self.log_file, level=logging.DEBUG, format=self.log_format)

    def writeDebugLog(self, entry):
        logging.debug(entry)

    def writeLog(self, entry):
        # default is Warn
        logging.warn(entry)

