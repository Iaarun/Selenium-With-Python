import logging


class GenerateLogs:

    @staticmethod
    def generatelog():
        '''
        this function will generate logs and store in Logs directory
        :return:  return logger
        '''

        logging.basicConfig(filename=".\\Logs\\automationexecution.log", format= '%(asctime)s: %(levelname)s: (message)s',
                            datefmt='%d-%b-%Y   %I:%M:%s 5p ')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
