import os
import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# ===================================================
Browser = os.path.abspath('') # Путь к лаунчеру браузера
Driver = os.path.abspath('') # Путь к драйверу браузера
# ===================================================

webdriver_service = service.Service(Driver)

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.binary_location = Browser
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, options=options)
try:
    wait = WebDriverWait(driver, 10)
    locators = ["//span[contains(text(),'Телевизоры')]",
        "//ul[@id='js-category-accordion']//div[contains(text(),'Телевизоры')]",
        "//div[@class='product-tile-add-to-basket-btn btn font-icon icon-trolley-cart ']"]

    driver.get('https://www.mvideo.ru')
    print(driver.find_element_by_xpath("//div[contains(text(),'Телевизоры')]"))
    s = EC.presence_of_element_located(driver.find_element_by_xpath("//div[contains(text(),'Телевизоры')]"))
    print(s)
    element = wait.until(lambda s: s)

    input_txt = driver.find_element_by_name('Ntt')
    input_txt.send_keys('телевизор\n')

    time.sleep(5)
finally:
    driver.quit()