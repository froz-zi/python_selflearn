"""Hari 2: 30 Hari pemrograman python"""


nama_depan = "fahrulrozi"
nama_belakang = "nasution"
nama_lengkap = nama_depan + " " + nama_belakang
negara = "indonesia"
kota = "bogor"
Usia = 23
tahun = 2002
is_married = False
is_true = True
is_light_on = True


print(nama_depan)
print(nama_belakang)
print(nama_lengkap)
print(negara)
print(kota)
print(Usia)
print(tahun)
print(is_married)
print(is_true)
print(is_light_on)

print(type(nama_depan))
print(type(nama_belakang))
print(type(nama_lengkap))
print(type(negara))
print(type(kota))
print(type(Usia))
print(type(tahun))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

len_nama = len(nama_lengkap)
print(len_nama)

panjang_nama_depan = len(nama_depan)
print(panjang_nama_depan)
panjang_nama_belakang = len(nama_belakang)
print(panjang_nama_belakang)
perbandingan = panjang_nama_depan - panjang_nama_belakang
print(perbandingan)

angka_satu = 5
angka_dua = 4
total_variabel = angka_satu + angka_dua
print(total_variabel)

variabe_diff = angka_dua - angka_satu
print(variabe_diff)

variabel_produk = angka_satu * angka_dua
print(variabel_produk)

pembagian_variabel = angka_satu / angka_dua
print(pembagian_variabel)   

sisa_variabel = angka_satu % angka_dua
print(sisa_variabel)

exp = angka_satu**angka_dua
print(exp)

floor_division = angka_satu // angka_dua
print(floor_division)

jari_jari = 30
_area_of_circle = 3.14 * jari_jari**2
print(_area_of_circle)

variabel_circum_of_circle = 2 * 3.14 * jari_jari
print(variabel_circum_of_circle)


input_radius = int(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = 3.14 * input_radius**2
print("Luas lingkaran dengan jari-jari", input_radius, "adalah:", luas_lingkaran)



input_nama = input("nama :")
input_umur = int(input("Umur"))
print("nama anda adalah : ", input_nama)
print("umur : ", input_umur)
help("keywords")