# 1. Tulis fungsi yang menghasilkan enam digit/karakter random_user_id.

import string
import random 
def random_user_id():
    karakter = string.ascii_lowercase + string.digits
    user_id = ""


    for i in range(6):
        user_id += random.choice(karakter)
    return user_id

print(random_user_id())

# 2. Ubah tugas sebelumnya.Deklarasikan fungsi bernama user_id_gen_by_user.Tidak memerlukan parameter apa pun tetapi
#  memerlukan dua masukan menggunakan masukan
# .Salah satu masukannya adalah jumlah karakter dan masukan kedua adalah jumlah ID yang seharusnya dihasilkan.

def user_id_gen_by_user():
    jml_karakter = int(input(" masukan jumlah karakter "))
    jumlah_id = int(input("jumalh id "))

    karakter =   string.digits + string.ascii_letters 

    for i in range(jumlah_id):
        user_id = ''.join(
            random.choice(karakter)
            for j in range (jml_karakter)
        )
        print(user_id)
        
import random


def rgb_color_gen():
    merah = random.randint(99, 255)
    hijau = random.randint(99, 255)
    biru = random.randint(99, 255)

    return f"rgb({merah},{hijau},{biru})"


print(rgb_color_gen())

# 1. Tulis fungsi list_of_hexa_colors yang mengembalikan sejumlah warna heksadesimal dalam 
# array enam angka heksadesimal yang ditulis setelah #.Sistem angka heksadesimal terbuat dari
#  16 simbol, 0-9 dan 6 huruf pertama alfabet, a-f.Periksa tugas 6 untuk contoh keluaran.

import random
import string


def list_of_hexa_colors(jumlah):
    karakter_hexa = string.digits + 'abcdef'
    daftar_warna = []

    for _ in range(jumlah):
        warna = '#' + ''.join(
            random.choice(karakter_hexa)
            for _ in range(6)
        )
        daftar_warna.append(warna)

    return daftar_warna


print(list_of_hexa_colors(3))#dari ai

# 1. Tulis fungsi list_of_rgb_colors yang mengembalikan sejumlah warna RGB dalam sebuah array.
import random


def list_of_rgb_colors(jumlah):
    daftar_warna = []

    for _ in range(jumlah):
        merah = random.randint(0, 255)
        hijau = random.randint(0, 255)
        biru = random.randint(0, 255)

        warna = f"rgb({merah}, {hijau}, {biru})"
        daftar_warna.append(warna)

    return daftar_warna


print(list_of_rgb_colors(3))#dari ai

# 1. Tulis fungsi menghasilkan warna yang dapat menghasilkan sejumlah warna hex atau rgb.

import random
import string


def generate_colors(jenis, jumlah):
    daftar_warna = []

    for _ in range(jumlah):
        if jenis == 'hexa':
            karakter = string.digits + 'abcdef'

            warna = '#' + ''.join(
                random.choice(karakter) for _ in range(6)
            )

        elif jenis == 'rgb':
            merah = random.randint(0, 255)
            hijau = random.randint(0, 255)
            biru = random.randint(0, 255)

            warna = f'rgb({merah}, {hijau}, {biru})'

        else:
            return 'Jenis warna harus hexa atau rgb'

        daftar_warna.append(warna)

    return daftar_warna


print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))#dari ai

# Panggil fungsi shuffle_list Anda, ia mengambil daftar sebagai parameter dan mengembalikan daftar 

import random


def shuffle_list(daftar):
    daftar_acak = daftar.copy()
    random.shuffle(daftar_acak)
    return daftar_acak


angka = [1, 2, 3, 4, 5]

print(shuffle_list(angka))
print(angka)

#1. Tulis fungsi yang mengembalikan array tujuh angka acak dalam rentang 0-9.Semua nomor harus unik.
import random


def tujuh_angka_unik():
    angka = random.sample(range(10), 7)
    return angka


print(tujuh_angka_unik())