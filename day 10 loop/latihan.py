# 1. Ulangi 0 hingga 10 menggunakan perulangan for, lakukan hal yang sama menggunakan perulangan while.
# 2. Iterasi 10 ke 0 menggunakan loop for, lakukan hal yang sama menggunakan loop while.


for data_itung in range(11):
    print(data_itung)

print ("="*10)

count = 0
while count <11 :
    print(count)
    count = count + 1

#2 
print ("="*10)
for data in range( 10 , -1 , -1):
    print(data)
print ("="*10)



data = 10

while data>= 0:
    print(data)
    data = data -1


# 3. Tulis sebuah loop yang membuat tujuh panggilan untuk mencetak, sehingga kita mendapatkan output segitiga berikut:

#    ```python
     #
##
###
####
#####
######
#######

for pagar in range (2 , 8):
    print("#"*pagar)

# 4. Gunakan loop bersarang untuk membuat yang berikut:

   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #

print ("="*10)

for kotak in range (8):
    print("# "*8)

# 5. Cetak pola berikut:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100

a = 1
b = 1 

for itung in range (10):
    hasil =  a * b


    print(f"{a} x {b} = {hasil}")
    a = a + 1
    b = b + 1




daftar = ['Python', 'Numpy','Pandas','Django']

for tampil in daftar:
    print(tampil)


# 7. Gunakan perulangan for untuk mengulangi dari 0 hingga 100 dan hanya mencetak angka genap
# 8. Gunakan perulangan for untuk mengulangi dari 0 hingga 100 dan hanya mencetak angka ganjil

for semua_angka in range(0, 101, 2):
    print(semua_angka)
for semua_angka in range(1, 101, 2):
    print(semua_angka)

# 1. Gunakan perulangan for untuk mengulangi dari 0 hingga 100 dan mencetak jumlah semua angka.
 
total = 0
for semua_angka2 in range(0, 101):
    total = total + semua_angka2
 
print ("total nya : ", total)


genap = 0
ganjil = 0
for  semua_angka3 in range (0, 101):
    if semua_angka3 % 2 == 0 :
        genap = genap + semua_angka3 
    else :
        ganjil = ganjil + semua_angka3


    
print("total genap ",genap)
print("total ganjil ",ganjil)




# 1. Buka folder data dan gunakan file tersebut.Ulangi negara-negara tersebut dan ekstrak semua negara yang mengandung kata _land_.
# 1. Ini adalah daftar buah, 'pisang', 'jeruk', 'mangga', 'lemon' urutan terbalik menggunakan loop.
# 1. Buka folder data dan gunakan file tersebut.
# 1. Berapa jumlah total bahasa dalam data
# 2. Temukan sepuluh bahasa yang paling banyak digunakan dari data
# 3. Temukan 10 negara dengan populasi terpadat di dunia

#1
from countries import countries 

print(countries[:5])

for country in countries:
    if 'land' in country:
        print(country)

#2
daftar_buah = ['pisang', 'jeruk', 'mangga', 'lemon']
for buah in reversed(daftar_buah):
    print(buah)
    
from countries_data import countries_data
total_bahasa = 0 
for bahasa in countries_data:
    print(bahasa["languages"])
    total_bahasa += 1
print("Total bahasa:", total_bahasa)

# 2. Temukan sepuluh bahasa yang paling banyak digunakan dari data
print("="*10)
from countries_data import countries_data
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:   
            language_count[language] = 1

sorted_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for language, total in sorted_languages[:10]:
    print(language, "-", total)

# 3. Temukan 10 negara dengan populasi terpadat di dunia

sorted_countries = sorted(
    countries_data,
    key=lambda country : country["population"],
    reverse = True
    
)

for country in sorted_countries[0:10]:
    print(country["name"], "-", country ["population"])
