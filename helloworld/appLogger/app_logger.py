import logging
from configparser import ConfigParser
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class AppLogger(object):
    __logger_instance = None

    def __init__(self):
        """ Virtually private constructor. """



    @staticmethod
    def initializeLogger():
        """ Static access method. """
        if AppLogger.__logger_instance == None:
            # AppLogger.__logger_instance = AppLogger()
            formatter = "%(asctime)s {app} [%(thread)d] %(levelname)-5s %(name)s - %(message)s. [file=%(filename)s:%(lineno)d]"
            #logging.basicConfig(format=formatter)
            logger = logging.getLogger("Rotating Log")
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter("%(asctime)s {app} [%(thread)d] %(levelname)-5s %(name)s - %(message)s. [file=%(filename)s:%(lineno)d]")
            currTimestamp = datetime.now()
            handler = TimedRotatingFileHandler("log/helloworld.log."+str(currTimestamp),
                                               when="s",
                                               interval=10,
                                               backupCount=5)
            handler.setFormatter(formatter)
            logger.addHandler(handler)


            AppLogger.__logger_instance = logger

    def __loadLogConfig(self):
        config = ConfigParser()
        config.read('logging.cfg')
        self.log_level = config['settings']['log_level']
        self.log_format = config['settings']['log_format']
        #self.log_format = "%(asctime)s {app} [%(thread)d] %(levelname)-5s %(name)s - %(message)s. [file=%(filename)s:%(lineno)d]"
        self.log_file = config['settings']['log_file']
        self.log_path = str(config['settings']['log_path'] + '/' + self.log_file)

        if self.log_level == "DEBUG":
            logging.basicConfig(filename=self.log_path, level=logging.DEBUG, format=self.log_format)

    @staticmethod
    def writeDebugLog(entry):
        if AppLogger.__logger_instance != None:
            AppLogger.__logger_instance.debug(entry)

    @staticmethod
    def writeLog(entry):
        # default is Warn
        if AppLogger.__logger_instance != None:
            AppLogger.__logger_instance.warn(entry)

    @staticmethod
    def writeInfoLog(string):
        if AppLogger.__logger_instance != None:
            AppLogger.__logger_instance.info(string)

