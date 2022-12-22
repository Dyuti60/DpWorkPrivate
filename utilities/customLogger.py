import logging

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        logging.basicConfig(filename=".\\logs\\automation.log",
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m-%d-%Y %H:%M:%S')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
        
