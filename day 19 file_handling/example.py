# - "r" - Baca - Nilai default.Membuka file untuk dibaca, ia mengembalikan kesalahan jika file tidak ada
# - "a" - Tambah - Membuka file untuk ditambahkan, membuat file jika tidak ada
# - "w" - Write - Membuka file untuk ditulis, membuat file jika tidak ada
# - "x" - Buat - Membuat file yang ditentukan, mengembalikan kesalahan jika file tersebut ada
# - "t" - Teks - Nilai default.Modus teks
# - "b" - Biner - Mode biner mis.gambar


# with open(r"C:\Users\Fahrul Rozi\Rozi\data.txt", "r") as file:
#     isi = file.read()
#     print(isi)

# f = open(r"C:\Users\Fahrul Rozi\Rozi\data.txt")
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()


# with open(r"C:\Users\Fahrul Rozi\Rozi\sata.txt", "w")as f:
#     f.write('This text will be written in a newly created file')




# with open(r"C:\Users\Fahrul Rozi\Rozi\bata.txt", "a") as file:
#     isi2 = file.add()
#     print(isi2)

with open(r"C:\Users\Fahrul Rozi\Rozi\data2.txt", "w") as f:
    f.write("Halo, ini teks baru")
    

with open(r"C:\Users\Fahrul Rozi\Rozi\data2.txt", "a") as f:
    f.write("\nIni teks tambahan")

with open(r"C:\Users\Fahrul Rozi\Rozi\baru.txt", "w") as f:
    f.write("Ini file baru")

import os
if os.path.exists(r"C:\Users\Fahrul Rozi\Rozi\baru.txt"):
    os.remove(r"C:\Users\Fahrul Rozi\Rozi\baru.txt")
else:
    print('The file does not exist')
