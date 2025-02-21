# Web Scrapper untuk web sscasn 2024

## Fungsi
Untuk mengumpulkan list formasi untuk CPNS berdasarkan jenjang pendidikan, jurusan dan pengadaan

## Dependency/Requirement
```
pip install pandas
pip install selenium
pip install openpyxl

```

## Pengunaan

pada bagian
```
detail = ["S-1/Sarjana", "S-1 INFORMATIKA", "CPNS"]

```
Silahkan ganti dengan urutan jenjang pendidikan, jurusan dan jenis pengadaan

jika ingin interaktif silahkan uncomment bagian :
```
# Aktifkan untuk input dinamis
# detail.append(input("Jenjang Pendidikan : "))
# detail.append(input("Program Studi : "))
# detail.append(input("Jenis Pengadaan : "))

```
dan comment bagian :
```
detail = ["S-1/Sarjana", "S-1 INFORMATIKA", "CPNS"]

```
## Hasil
contoh hasil dapat dilihat pada daftar_formasi.csv dan daftar_formasi.xlsx