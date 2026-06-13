# 1. Buat kamus kosong bernama dog
# 2. Tambahkan nama, warna, ras, kaki, umur ke kamus anjing
# 3. Buat kamus siswa dan tambahkan nama depan, nama belakang, jenis kelamin, usia, status perkawinan, keterampilan, negara, kota dan alamat sebagai kunci kamus
# 4. Dapatkan panjang kamus siswa
# 5. Dapatkan nilai skill dan periksa tipe datanya, harus berupa daftar
# 6. Ubah nilai keterampilan dengan menambahkan satu atau dua keterampilan
# 7. Dapatkan kunci kamus sebagai daftar
# 8. Dapatkan nilai kamus sebagai daftar
# 9. Ubah kamus menjadi daftar tupel menggunakan metode _items_
# 10. Hapus salah satu item dalam kamus
# 11. Hapus salah satu kamus

dog = {
    "nama":"anjay",
    "warna" : "hitam",
    "ras" : "golden",
    "umur" : 3 

}

siswa = {
    "nama_depan" : "budi",
    "nama_belakang" : "tabuti",
    "jenis_kelamin": "jantan ",
    "status" : False,
    "alamat" : "Bandung",
    "keterampilan" : ["ipa","ips"] 
  
}

print(len(siswa))
print(siswa.get("nama_depan"))
print(type(siswa["nama_depan"]))  # Cek tipe data dari nilai dictionary
print(type(siswa))

data_tuple = tuple(siswa.items())
print(type(data_tuple))
del siswa["status"]
print(siswa)    