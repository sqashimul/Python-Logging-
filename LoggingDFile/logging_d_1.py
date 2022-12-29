import logging
logging.basicConfig(level = logging.DEBUG, filename = "..\logs\dlogs1.log", filemode="a",
                    format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

class DLogging1:
    def add_numbers(self, a, b):
        return a + b

    def multiply_numbers(self, a, b):
        return a * b

dl = DLogging1()
sum_result = dl.add_numbers(3, 5)
logging.debug("debug: addition of numbers is: {}".format(sum_result))
logging.info("info: addition of numbers is: {}".format(sum_result))
logging.warning("warning addition of numbers is: {}".format(sum_result))
logging.error("error addition of numbers is: {}".format(sum_result))
logging.critical("critical: addition of numbers is: {}".format(sum_result))

multiply_result = dl.multiply_numbers(3, 5)
logging.warning("The multiplication of numbers is: {}".format(multiply_result))
