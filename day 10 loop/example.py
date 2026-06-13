# while condition:
#     code goes here





count = 0
while count < 5:
    print(count)
    count = count + 1
# mencetak dari 0 hingga 4


# Pada perulangan while di atas, kondisi menjadi salah ketika hitungannya 5. Saat itulah perulangan berhenti.
# Jika kita tertarik untuk menjalankan blok kode setelah kondisinya tidak lagi benar, kita bisa menggunakan _else_.


# # sintaksis
# while condition:
#     code goes here
# else:
#     code goes here





count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


# Kondisi perulangan di atas akan menjadi salah ketika hitungannya 5 dan perulangan berhenti, dan eksekusi memulai pernyataan else.Hasilnya 5 akan dicetak.

### Istirahat dan Lanjutkan - Bagian 1

# - Break: Kita menggunakan break ketika kita ingin keluar atau menghentikan perulangan.


# # sintaksis
# while condition:
#     code goes here
#     if another_condition:
#         break





count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


# Perulangan while di atas hanya mencetak 0, 1, 2, tetapi ketika mencapai 3 berhenti.

# - Lanjutkan: Dengan pernyataan lanjutkan kita dapat melewati iterasi saat ini, dan melanjutkan dengan iterasi berikutnya:


# # sintaksis
# while condition:
#     code goes here
#     if another_condition:
#         continue





count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1


# Perulangan while di atas hanya mencetak 0, 1, 2 dan 4 lompatan 3.

# ### Untuk Lingkaran

# Kata kunci _for_ digunakan untuk membuat perulangan for, mirip dengan bahasa pemrograman lain, tetapi dengan beberapa perbedaan sintaksis.Loop digunakan untuk mengulangi urutan yang berupa daftar, tupel, kamus, himpunan, atau string.

# -Menggunakan loop For pada daftar


# # sintaksis
# for iterator in lst:
#     code goes here





numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number adalah nama sementara untuk merujuk ke item daftar, hanya valid di dalam loop ini
    print(number)  # angka-angka tersebut akan dicetak baris demi baris, dari 0 hingga 5


# -Menggunakan loop For pada string


# # sintaksis
# for iterator in string:
#     code goes here





language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])


# -Menggunakan loop For pada tuple


# # sintaksis
# for iterator in tpl:
#     code goes here





numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# - Untuk loop dengan kamus
# Mengulangi kamus memberi Anda kunci kamus.


# # sintaksis
# for iterator in dct:
#     code goes here





person = {
    'first_name':'vincen',
    'last_name':'babi',
    'age':250,
    'country':'indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # dengan cara ini kita mencetak kunci dan nilai


# -Menggunakan For Loop di set


# # sintaksis
# for iterator in st:
#     code goes here





it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


### Istirahat dan Lanjutkan - Bagian 2

# Pengingat singkat:
# _Break_: Kita menggunakan break ketika kita ingin menghentikan perulangan kita sebelum selesai.


# # sintaksis
# for iterator in sequence:
#     code goes here
#     if condition:
#         break





numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break


# Dalam contoh di atas, perulangan berhenti ketika mencapai 3.

# Lanjutkan: Kita menggunakan continue ketika kita ingin melewati beberapa langkah dalam iterasi perulangan.


# # sintaksis
# for iterator in sequence:
#     code goes here
#     if condition:
#         continue





numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")  # untuk kondisi tangan pendek memerlukan pernyataan if dan else
print('outside the loop')


# Pada contoh di atas, jika angkanya sama dengan 3, langkah _setelah_ kondisi tetapi di dalam perulangan dilewati dan eksekusi perulangan dilanjutkan jika masih ada iterasi yang tersisa.

# ### Fungsi Jangkauan

# Fungsi _range_ digunakan untuk mengembalikan daftar angka._rangestart, end, step_ mengambil tiga parameter: awal, akhir, dan kenaikan.Secara default dimulai dari 0 dan kenaikannya adalah 1. Urutan rentang memerlukan setidaknya 1 akhir argumen.
# Membuat urutan menggunakan rentang


lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # 2 argumen menunjukkan awal dan akhir urutan, langkah disetel ke default 1
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st)  # {0, 2, 4, 6, 8, 10}

# untuk mundur dari awal sampai akhir
lst = list(range(11,0,-2))
print(lst)  # [11,9,7,5,3,1]



# # sintaksis
# for iterator in range(start, end, step):





for number in range(11):
    print(number)  # mencetak 0 hingga 10, tidak termasuk 11


### Bersarang Untuk Loop

# Kita dapat menulis loop di dalam satu loop.


# # sintaksis
# for x in y:
#     for t in x:
#         print(t)





person = {
    'first_name': 'vincen',
    'last_name': 'babi',
    'age': 250,
    'country': 'indo',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)


### Untuk Yang Lain

# Jika kita ingin mengeksekusi beberapa pesan ketika loop berakhir, kita menggunakan yang lain.


# # sintaksis
# for iterator in range(start, end, step):
#     do something
# else:
#     print('The loop ended')





for number in range(11):
    print(number)  # mencetak 0 hingga 10, tidak termasuk 11
else:
    print('The loop stops at', number)


### Lulus

# Dalam python ketika pernyataan diperlukan setelah titik koma, tetapi kami tidak ingin mengeksekusi kode apa pun di sana, kami dapat menulis kata _pass_ untuk menghindari kesalahan.Kita juga bisa menggunakannya sebagai pengganti, untuk pernyataan di masa depan.




for number in range(6):
    pass