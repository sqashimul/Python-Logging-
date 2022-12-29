import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.yatra.com/")

driver.find_element(By.XPATH, "//a[@title='Round Trip']").click()
driver.find_element(By.NAME, "flight_origin").send_keys("DEL")
driver.find_element(By.NAME, "flight_destination").send_keys("HYD")

driver.find_element(By.ID, "BE_flight_origin_date").send_keys("12/01/2023")
# driver.find_element(By.ID, "12/01/2023").click()
driver.find_element(By.ID, "BE_flight_arrival_date").send_keys("16/01/2023")
# driver.find_element(By.ID, "16/01/2023").click()
time.sleep(4)

# driver.find_element(By.ID, "BE_flight_flsearch_btn").click()
driver.find_element(By.ID, "BE_flight_flsearch_btn").click()
time.sleep(4)