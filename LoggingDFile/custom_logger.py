import inspect
import logging
class CustLogger:
    def custom_logger(self, logLevel = logging.DEBUG):
        # Set class/method name frome where its called
        logger_name = inspect.stack()[1][3]
        # creat logger
        logger = logging.getLogger()
        logger.setLevel(logLevel)

        fh = logging.FileHandler("automation.log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


lod = CustLogger()
lod.custom_logger()

