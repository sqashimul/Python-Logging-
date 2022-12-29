import logging

import logger_d
logging.basicConfig(level = logging.DEBUG, filename = "..\logs\dlogs1.log", filemode="a",
                    format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

logging.debug("debug log staement")
logging.info("info log statement")
logging.warning("warning log statement")
logging.error("error log statement")
logging.critical("critical log statement")
