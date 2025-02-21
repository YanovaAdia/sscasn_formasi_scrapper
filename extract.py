from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.firefox.options import Options
import time

detail = ["S-1/Sarjana", "S-1 ILMU INFORMATIKA", "CPNS"]

# detail.append(input("Jenjang Pendidikan : "))
# detail.append(input("Program Studi : "))
# detail.append(input("Jenis Pengadaan : "))

detail.reverse()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://sscasn.bkn.go.id/')
time.sleep(2)


input_seq = (1,2,4)

for seq in input_seq:
    item = detail.pop()
    in_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/div/input')
    in_keys.click()
    in_keys.send_keys(item)
    set_keys = driver.find_element(By.XPATH, f'//form/div/div[{seq}]/div/div/ul/li[1]')
    set_keys.click()


set_keys = driver.find_element(By.XPATH, "//form/div/div[5]/a")
set_keys.click()
time.sleep(2)

next_button = driver.find_element(By.CLASS_NAME, "ant-pagination-next")


while True:

    temp_data = {
    "jabatan" : [],
    "instansi" : [],
    "unit_kerja" : [],
    "formasi" : [],
    "khusus_atau_disabilitas" : [],
    "penghasilan_min" : [],
    "penghasilan_max" : [],
    "kebutuhan" : [],
    "verifikasi" : [] # Dapat dihapus jika pda masa administrasi (belum ada verifikasi)
}
col = driver.find_elements(By.XPATH, f'//table/tbody/tr')

for i in range(len(col)):
    row = driver.find_elements(By.XPATH, f'//table/tbody/tr[{i+1}]/td')

    temp_data["jabatan"].append(row[0].text)
    temp_data["instansi"].append(row[1].text)
    temp_data["unit_kerja"].append(row[2].text)
    temp_data["formasi"].append(row[3].text)
    temp_data["khusus_atau_disabilitas"].append(row[4].text)
    split_salary = row[5].text.replace(',', '.').split(' - ')
    temp_data["penghasilan_min"].append(split_salary[0])
    temp_data["penghasilan_max"].append(split_salary[1])
    temp_data["kebutuhan"].append(row[6].text)
    temp_data["verifikasi"].append(row[7].text)

    if next_button.is_enabled() == False:
        break;
    driver.execute_script("arguments[0].click();", next_button)

df = pd.DataFrame(temp_data, index=None)
df.to_csv("data_formasi.csv", index=False)
driver.quit()