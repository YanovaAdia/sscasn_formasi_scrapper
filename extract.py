from selenium import webdriver
from selenium.webdriver.common.by import By
import time

detail = []

detail.append(input("Jenjang Pendidikan : "))
detail.append(input("Program Studi : "))
detail.append(input("Jenis Pengadaan : "))

detail.reverse()

driver = webdriver.Firefox()
driver.get('https://sscasn.bkn.go.id/')
driver.implicitly_wait(2)

input_seq = (1,2,4)

for seq in input_seq:
    in_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/div/input[1]')
    in_keys.send_keys(detail.pop())
    driver.implicitly_wait(1)
    set_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/ul/li[1]')
    set_keys.click()

driver.implicitly_wait(2)
set_keys = driver.find_element(By.XPATH, "//form/div/div[5]/a")
set_keys.click()
# el_pend = driver.find_element(By.XPATH, "//form/div/div[2]/div/div/div/input[1]")
# el_pend.send_keys("SMK REKAYASA PERANGKAT LUNAK")

# el_pend = driver.find_element(By.XPATH, "//form/div/div[4]/div/div/div/input[1]")
# el_pend.send_keys("CPNS")

