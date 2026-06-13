## Modul

### Apa itu Modul

# Modul adalah file yang berisi sekumpulan kode atau sekumpulan fungsi yang dapat dimasukkan ke dalam aplikasi.Modul dapat berupa file yang berisi variabel tunggal, fungsi, atau basis kode besar.

### Membuat Modul

# Untuk membuat modul, kami menulis kode kami dalam skrip python dan kami menyimpannya sebagai file .py.Buat file bernama mymodule.py di dalam folder proyek Anda.Mari kita tulis beberapa kode di file ini.


# file mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


# Buat file main.py di direktori proyek Anda dan impor file mymodule.py.

### Mengimpor Modul

# Untuk mengimpor file kita menggunakan kata kunci _import_ dan nama file saja.


# file utama.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'JKT'))  # Keterbukaan Informasi


### Impor Fungsi dari Modul

# Kita dapat memiliki banyak fungsi dalam satu file dan kita dapat mengimpor semua fungsi secara berbeda.


# file utama.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Vincen','JKT'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])


### Impor Fungsi dari Modul dan Mengganti Nama

# Selama mengimpor kita dapat mengganti nama modul.


# file utama.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Vincen','JKT'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])


## Impor Modul Bawaan

# Seperti bahasa pemrograman lainnya kita juga dapat mengimpor modul dengan mengimpor file/fungsi menggunakan kata kunci _import_.Mari impor modul umum yang paling sering kita gunakan.Beberapa modul bawaan yang umum: _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_

# ### Modul OS

# Dengan menggunakan modul python _os_ dimungkinkan untuk melakukan banyak tugas sistem operasi secara otomatis.Modul OS di Python menyediakan fungsi untuk membuat, mengubah direktori kerja saat ini, dan menghapus folder direktori, mengambil isinya, mengubah dan mengidentifikasi direktori saat ini.


# impor modul
import os
# Membuat direktori
os.mkdir('directory_name')
# Mengubah direktori saat ini
os.chdir('path')
# Mendapatkan direktori kerja saat ini
os.getcwd()
# Menghapus direktori
os.rmdir()


### Modul Sistem

# Modul sys menyediakan fungsi dan variabel yang digunakan untuk memanipulasi berbagai bagian lingkungan runtime Python.Fungsi sys.argv mengembalikan daftar argumen baris perintah yang diteruskan ke skrip Python.Item pada indeks 0 dalam daftar ini selalu merupakan nama skrip, pada indeks 1 adalah argumen yang diteruskan dari baris perintah.

# Contoh file script.py:


import sys
# print(sys.argv[0], argv[1],sys.argv[2]) # baris ini akan dicetak: nama file argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


# Sekarang untuk memeriksa cara kerja skrip ini saya menulis di baris perintah:

# sh
# python script.py Asabeneh 30DaysOfPython


# Hasilnya:

# sh
# Welcome Asabeneh. Enjoy  30DayOfPython challenge! 


# Beberapa perintah sistem yang berguna:


# untuk keluar dari sistem
sys.exit()
# Untuk mengetahui variabel bilangan bulat terbesar dibutuhkan
sys.maxsize
# Untuk mengetahui jalur lingkungan
sys.path
# Untuk mengetahui versi python yang Anda gunakan
sys.version


### Modul Statistik

# Modul statistik menyediakan fungsi untuk statistik matematika dari data numerik.Fungsi statistik populer yang didefinisikan dalam modul ini: _mean_, _median_, _mode_, _stdev_ dll.


from statistics import *  # mengimpor semua modul statistik
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))  # ~22.9
print(median(ages))  # 23
print(mode(ages))  # 20
print(stdev(ages))  # ~2.3


### Modul Matematika

# Modul yang berisi banyak operasi matematika dan konstanta.


import math
print(math.pi)  # 3.141592653589793, konstanta pi
print(math.sqrt(2))  # 1.4142135623730951, akar kuadrat
print(math.pow(2, 3))  # 8.0, fungsi eksponensial
print(math.floor(9.81))  # 9, pembulatan ke yang terendah
print(math.ceil(9.81))  # 10, pembulatan ke angka tertinggi
print(math.log10(100))  # 2, logaritma dengan 10 sebagai basis


# Sekarang, kita telah mengimpor modul *math* yang berisi banyak fungsi yang dapat membantu kita melakukan perhitungan matematis.Untuk memeriksa fungsi apa saja yang dimiliki modul, kita dapat menggunakan _helpmath_, atau _dirmath_.Ini akan menampilkan fungsi-fungsi yang tersedia dalam modul.Jika kita hanya ingin mengimpor fungsi tertentu dari modul, kita mengimpornya sebagai berikut:


from math import pi
print(pi)


# Dimungkinkan juga untuk mengimpor beberapa fungsi sekaligus



from math import pi, sqrt, pow, floor, ceil, log10
print(pi)  # 3.141592653589793
print(sqrt(2))  # 1.4142135623730951
print(pow(2, 3))  # 8.0
print(floor(9.81))  # 9
print(ceil(9.81))  # 10
print(math.log10(100))  # 2



# Tetapi jika kita ingin mengimpor semua fungsi dalam modul matematika kita dapat menggunakan \* .


from math import *
print(pi)  # 3.141592653589793, konstanta pi
print(sqrt(2))  # 1.4142135623730951, akar kuadrat
print(pow(2, 3))  # 8.0, eksponensial
print(floor(9.81))  # 9, pembulatan ke yang terendah
print(ceil(9.81))  # 10, pembulatan ke angka tertinggi
print(math.log10(100))  # 2


# Saat kita mengimpor kita juga bisa mengganti nama fungsinya.


from math import pi as  PI
print(PI)  # 3.141592653589793


### Modul Tali

# Modul string adalah modul yang berguna untuk berbagai tujuan.Contoh di bawah ini menunjukkan beberapa penggunaan modul string.


import string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


### Modul Acak

# Sekarang Anda sudah familiar dengan mengimpor modul.Mari kita lakukan satu kali impor lagi agar lebih memahaminya.Mari kita impor modul _random_ yang memberi kita angka acak antara 0 dan 0,9999.... Modul _random_ memiliki banyak fungsi tetapi di bagian ini kita hanya akan menggunakan _random_ dan _randint_.


from random import random, randint
print(random())  # tidak diperlukan argumen apa pun;ia mengembalikan nilai antara 0 dan 0,9999
print(randint(5, 20))  # ia mengembalikan bilangan bulat acak antara [5, 20] inklusif
