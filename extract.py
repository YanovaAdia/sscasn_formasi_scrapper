from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

detail = ["S-1/Sarjana", "S-1 PERPUSTAKAAN", "CPNS"]

# detail.append(input("Jenjang Pendidikan : "))
# detail.append(input("Program Studi : "))
# detail.append(input("Jenis Pengadaan : "))

detail.reverse()

driver = webdriver.Firefox()
driver.get('https://sscasn.bkn.go.id/')
time.sleep(3)


input_seq = (1,2,4)

for seq in input_seq:
    item = detail.pop()
    in_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/div/input')
    in_keys.click()
    in_keys.send_keys(item)
    time.sleep(1)
    set_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/ul/li[1]')
    time.sleep(1)
    set_keys.click()


set_keys = driver.find_element(By.XPATH, "//form/div/div[5]/a")
set_keys.click()


next_button = driver.find_element(By.CLASS_NAME, "ant-pagination-item-link").is_enabled()
print(next_button)
