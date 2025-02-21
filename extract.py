from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.firefox.options import Options
import time

def clear_dict():
    
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
    return temp_data

def hitung_page(total):
    len_page = 0
    while True:
        if total <= 10:
            len_page += 1
            break

        total -= 10
        len_page += 1
    return len_page

# hanya untuk testing
detail = ["S-1/Sarjana", "S-1 INFORMATIKA", "CPNS"]

# Aktifkan untuk input dinamis
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

try :

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

    main_df = pd.DataFrame(clear_dict())

    total_item = driver.find_element(By.CLASS_NAME, "ant-pagination-total-text")

    total = int(total_item.text.split(" ")[2])

    for i in range(hitung_page(total)):
        time.sleep(2)
        temp_data = clear_dict()
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

        driver.execute_script("arguments[0].click();", next_button)

        df = pd.DataFrame(temp_data, index=None)
        main_df = pd.concat([main_df, df], axis=0, ignore_index=True)
except:
    print("Error Mulai ulang program")
    exit()


main_df.to_csv("data_formasi.csv", index=False)
main_df.to_excel("data_formasi.xlsx", index=False)
driver.quit()