import logging
class LoggerD:
    def sample_logger(self):
        #create logger
        logger = logging.getLogger(LoggerD.__name__)
        logger.setLevel(logging.DEBUG)
        #create console handler or file handler and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler("demologfile.log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        # add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)
        # add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        # application code - log message
        logger.debug("debug log staement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")

lod = LoggerD()
lod.sample_logger()



