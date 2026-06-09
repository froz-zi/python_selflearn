umur = 23
tinggi = 170.0

a = 5 + 4j

# alas  = int(input("Masukan alas : "))
# tinggi = int(input("Masukan tinggi :  "))
# luas_segitiga = 0.5*alas*tinggi
# print(int(luas_segitiga))

# sisi_1 = int(input("Masukan sisi 1 "))
# sisi_2 = int(input("Masukan sisi 2 "))
# sisi_3 = int(input("Masukan sisi 3 "))

# keliling_segitiga = sisi_1 + sisi_2 + sisi_3
# print(keliling_segitiga)

# Nomor 8
# Persamaan: y = 2x - 2
# Bentuk umum: y = mx + c

# m1 = 2
# c = -2

# # Titik potong y terjadi saat x = 0
# titik_potong_y = (0, c)

# # Titik potong x terjadi saat y = 0
# # 0 = mx + c
# # x = -c / m
# x_intercept = -c / m1
# titik_potong_x = (x_intercept, 0)

# print("Nomor 8")
# print("Kemiringan:", m1)
# print("Titik potong x:", titik_potong_x)
# print("Titik potong y:", titik_potong_y)


# # Nomor 9
# # Rumus kemiringan:
# # m = (y2 - y1) / (x2 - x1)

# x1, y1 = 2, 2
# x2, y2 = 6, 10

# m2 = (y2 - y1) / (x2 - x1)

# print("\nNomor 9")
# print("Kemiringan antara titik (2, 2) dan (6, 10):", m2)


# # Nomor 10
# print("\nNomor 10")

# if m1 > m2:
#     print("Kemiringan nomor 8 lebih besar dari nomor 9")
# elif m1 < m2:
#     print("Kemiringan nomor 9 lebih besar dari nomor 8")
# else:
#     print("Kemiringan nomor 8 dan nomor 9 sama")



#11. Hitung nilai y y = x^2 + 6x + 9. Coba gunakan nilai x yang berbeda dan cari tahu berapa nilai x y yang akan menjadi 0.

for x in range (-100, 100):
    y = x**2 + 6*x + 9

    print("x = ", x , "y = ", y)

    if y == 0 :
        print("nilai x nya adalah : ", x)


#12 Temukan panjang 'python' dan 'naga' dan buatlah pernyataan perbandingan yang salah.

data_1 = "python"
data_2 = "naga"
print(len(data_1))
print(len(data_2))

pernyataan = data_1 is data_2
print(pernyataan)

#13. Gunakan operator _and_ untuk memeriksa apakah 'on' ditemukan di 'python' dan 'dragon'

# data_3 = "on"   
# pernyataan_2 = data_3 is pernyataan
# print(pernyataan_2)
kata_1 = "python"
kata_2 = "dragon"

pernyataan_2 = "on" in kata_1 and "on" in kata_2

print("Apakah 'on' ada di python dan dragon?", pernyataan_2)


#14. _Saya harap kursus ini tidak penuh jargon_.Gunakan operator _in_ untuk memeriksa apakah _jargon_ ada dalam kalimat.


print('jargon' in 'Saya harap kursus ini tidak penuh jargon') 

# 15. Tidak ada 'on' pada dragon dan python
print('on' not in 'dragon' and 'on' not in 'python')

#16 Temukan panjang teks _python_ dan ubah nilainya menjadi float dan ubah menjadi string

a15 = "python"
hasil = (len(a15))
print(hasil)
print(type(hasil))

ubahfloat = float(hasil)
print(ubahfloat)
print(type(ubahfloat))

ubahstr = str(ubahfloat)
print(ubahstr)
print(type(ubahstr))

#17 Bilangan genap habis dibagi 2 dan sisanya nol.Bagaimana cara memeriksa suatu bilangan genap atau tidak menggunakan python?

# angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print("Bilangan genap")
else:
    print("Bilangan ganjil")

18 Periksa apakah pembagian lantai 7 dengan 3 sama dengan nilai konversi int sebesar 2,7.

a18 = 7 // 3
b18 = int(2.7)

print("Hasil 7 // 3:", a18)
print("Hasil int(2.7):", b18)

print(a18 == b18)


# #19. Periksa apakah tipe '10' sama dengan tipe 10
print (" === 19 === ")
a19 = '10'
b19 = 10

# print(a19 is b19)

# # 20. Periksa apakah int'9.8' sama dengan 10
print (" === 20 === ")
a20 = 9.8
b20 = 10 
print(a20 is b20)

# # 21. Tulis skrip yang meminta pengguna memasukkan jam dan tarif per jam.Hitung gaji orang tersebut?
print (" === 21 === ")

a21 = int(input("enter hour : "  ))
b21 = int(input("enter rate per hour : "  ))
c21 = a21 * b21 
print("your weekly earning is ",c21)

# # 22. Tulis skrip yang meminta pengguna memasukkan jumlah tahun.Hitung berapa detik seseorang dapat hidup.Asumsikan seseorang dapat hidup ratusan tahun
print (" === 22 === ")
a22 = int(input("enter number years u lived : "))
b22 = a22*31536000
print ("anda telah hidup selama ", b22, 'detik')


'''23. Tulis skrip Python yang menampilkan tabel berikut
python
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

for x in range(1, 6):
    print(x, x**0, x**1, x**2, x**3)