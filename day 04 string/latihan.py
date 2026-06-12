# 1. Gabungkan string 'Thirty', 'Days', 'Of', 'Python' menjadi satu string, 'Thirty Days Of Python'.
print('=== no 1 ===')
a1 = 'thirty'
b1 = 'Days'
c1 = 'of'
d1 = 'Python'

print(a1,b1,c1,d1)

# 2. Gabungkan string 'Coding', 'For' , 'All' menjadi satu string, 'Coding For All'.
print('=== no 2 ===')
a2 = 'Coding' 
b2 = 'For' 
c2 = 'All'

gabungan2 = a2 +''+ b2+'' + c2
print(gabungan2)

# 3.Deklarasikan variabel bernama perusahaan dan tetapkan ke nilai awal "Coding Untuk Semua".

perusahaan = 'Coding Untuk Semua'


# 4.Cetak variabel perusahaan menggunakan _print_.
print('=== no 4 ===')
print(perusahaan)

# 5. Cetak panjang string perusahaan menggunakan metode _len_ dan _print_.
print('=== no 5 ===')
print(len(perusahaan))

# 6. Ubah semua karakter menjadi huruf besar menggunakan metode _upper_.
print('=== no 6 ===')
print(perusahaan.upper())

# 7. Ubah semua karakter menjadi huruf kecil menggunakan metode _lower_.
print('=== no 7 ===')
print(perusahaan.lower())

# 8. Gunakan metode kapitalisasi, judul, swapcase untuk memformat nilai string _Coding For All_.
print('=== no 8 ===')
print(perusahaan.title())

#9. Potong kata pertama dari string _Coding For All_.
print('=== no 9 ===')
potong_kata = perusahaan.split()
print(potong_kata[1],potong_kata[2])

# 10. Periksa apakah string _Coding For All_ berisi kata Coding menggunakan metode indeks, temukan atau metode lainnya.
print('=== no 10 ===')
print('Coding'in perusahaan)

# 11. Ganti kata coding pada string 'Coding For All' dengan Python.
print('=== no 11 ===')
hasil11 = perusahaan.replace("Coding", "python")
print(hasil11)

# 12. Ubah “Python for Everyone” menjadi “Python for All” dengan menggunakan metode replace atau cara lainnya.
print('=== no 12 ===')
ubah12 = perusahaan.replace("Coding Untuk Semua", "Python Untuk Semua")
print(ubah12)

# 13. Pisahkan string 'Coding For All' menggunakan spasi sebagai pemisah split .
print('=== no 13 ===')
ubah_13 = perusahaan.split()
print(ubah_13)

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" pisahkan string dengan koma.
data14 = 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
print(data14)

# 15. Apa karakter pada indeks 0 pada string _Coding For All_.

print(perusahaan[0])

# 16. Berapakah indeks terakhir dari string _Coding For All_.
print(perusahaan[-1])
#17. Karakter apa yang ada di indeks 10 pada string "Coding For All".

print(perusahaan[10])

#18 Buatlah akronim atau singkatan dari nama 'Python For Everyone'.
kata18 = ubah12.split()
akronim18 = kata18[0][0] + kata18[1][0]+ kata18[2][0]
print(akronim18)

#19. Buatlah akronim atau singkatan dari nama 'Coding For All'.

kata19 = perusahaan.split()
akronim19 = kata19[0][0] + kata19[1][0]+ kata19[2][0]
print(akronim19)

# 20. Gunakan indeks untuk menentukan posisi kemunculan pertama C pada Coding For All.
print(perusahaan.index("C"))

#21. Gunakan indeks untuk menentukan posisi kemunculan pertama F pada Coding For All.
print(perusahaan.index("U"))

#22. Gunakan rfind untuk menentukan posisi kemunculan terakhir l pada Coding For All People.
print(perusahaan.rfind('u'))
print(perusahaan.find('u'))
# 23. Gunakan indeks atau find untuk mencari posisi kemunculan pertama kata 'karena' pada kalimat berikut: 'Anda tidak dapat mengakhiri kalimat dengan karena karena merupakan konjungsi'
kalimat23 = 'Anda tidak dapat mengakhiri kalimat dengan karena karena merupakan konjungsi'
print(kalimat23.find('karena'))
# 13. Pisahkan string 'Coding For All' menggunakan spasi sebagai pemisah split .
print('=== no 24 ===')
#24. Gunakan rindex untuk mencari posisi kemunculan terakhir kata because pada kalimat berikut: 'kalimat tidak boleh diakhiri dengan because because because merupakan konjungsi'
kalimat24 = 'kalimat tidak boleh diakhiri dengan because because because merupakan konjungsi'
print(kalimat24.rindex('because'))
#25 Potonglah kalimat 'karena karena' pada kalimat berikut: 'Kamu tidak bisa mengakhiri kalimat dengan karena karena karena merupakan konjungsi'
kalimat25 = 'Kamu tidak bisa mengakhiri kalimat dengan karena karena karena merupakan konjungsi'
hasil_potong25 = kalimat25.replace('karena karena ', '')
print(hasil_potong25)

# 26. Carilah posisi kemunculan pertama kata 'karena' pada kalimat berikut: 'Kalimat tidak boleh diakhiri dengan karena karena merupakan konjungsi'
kalimat26 = 'Kalimat tidak boleh diakhiri dengan karena karena merupakan konjungsi'
print(kalimat26.find('karena'))

print('=== no 27 ===')
#27. Potonglah kalimat 'karena karena karena' pada kalimat berikut: 'Kamu tidak bisa mengakhiri kalimat dengan karena karena karena merupakan konjungsi'
kalimat_27 =  'Kamu tidak bisa mengakhiri kalimat dengan karena karena karena merupakan konjungsi'
hasil_potong_27 = kalimat_27.replace('karena karena karena', '')
print(hasil_potong_27)

# 28. Apakah 'Coding Untuk Semua' dimulai dengan substring _Coding_?
print(perusahaan.startswith('Coding'))

#29. Apakah 'Coding For All' diakhiri dengan substring _coding_?
print(perusahaan.endswith('Semua'))

#30. '&nbsp;&nbsp;Pengkodean Untuk Semua &nbsp;&nbsp;&nbsp;&nbsp;'&nbsp;, hapus spasi tambahan kiri dan kanan pada string yang diberikan.


hasil = perusahaan.strip()

print(hasil)

nama = "   Fahrul Rozi   "

print(nama)
print(nama.strip())