from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Chrome('C:\\python\\chromedriver.exe')
#driver.get("https://auto.ru/cars/used/sale/volkswagen/tiguan/1106535053-5df523be/")


url= "https://auto.ru/cars/used/sale/volkswagen/tiguan/1106535053-5df523be/"
#driver.find_element(By.CSS_SELECTOR, 'OfferPhone__content').click()



# title_class = driver.find_elements(By.CSS_SELECTOR, "button")

# for el in title_class:
#     if el.text == "Показать телефон":
#         login_button = el
#         login_button.click()





try:
    driver.get(url=url)
    time.sleep(10)
except Exception as ex:
        print(ex)

finally: 
    driver.close()
    driver.quit()

