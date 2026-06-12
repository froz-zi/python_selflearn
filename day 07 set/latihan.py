### Latihan: Tingkat 1

# 1. Tentukan panjang himpunan it_companies
# 2. Tambahkan 'Twitter' ke it_companies
# 3. Masukkan beberapa perusahaan IT sekaligus ke kumpulan it_companies
# 4. Hapus salah satu perusahaan dari kumpulan it_companies
# 5. Apa perbedaan antara hapus dan buang

# ### Latihan: Tingkat 2

# 1. Bergabunglah dengan A dan B
# 2. Temukan persimpangan A B
# 3. Merupakan himpunan bagian dari B
# 4. Apakah himpunan lepas A dan B
# 5. Gabungkan A dengan B dan B dengan A
# 6. Berapakah selisih simetris antara A dan B
# 7. Hapus set sepenuhnya

# ### Latihan: Tingkat 3

# 1. Ubah umur menjadi suatu himpunan dan bandingkan panjang daftar dan himpunan tersebut, mana yang lebih besar?
# 2. Jelaskan perbedaan tipe data berikut: string, list, tuple dan set
# 3. _Saya seorang guru dan saya suka menginspirasi dan mengajar orang._ Berapa banyak kata unik yang digunakan dalam kalimat tersebut?Gunakan metode split dan atur untuk mendapatkan kata-kata unik.





it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Tentukan panjang himpunan it_companies
print(len(it_companies))
# 2. Tambahkan 'Twitter' ke it_companies
it_companies.add('Twitter')
print(it_companies)
# 3. Masukkan beberapa perusahaan IT sekaligus ke kumpulan it_companies
it_companies.update(['Adobe', 'Samsung'])
print(it_companies)
# 4. Hapus salah satu perusahaan dari kumpulan it_companies
it_companies.remove('Facebook')
print(it_companies)


# 1. Bergabunglah dengan A dan B
gabungan = A.union(B)
gabungan_berurut= sorted(gabungan)
print(gabungan_berurut)

# persimpangan itu kedua nilai di variabel yang berbeda
# 2. Temukan persimpangan A B

persimpangan = A.intersection(B)
print(persimpangan) 

# 3. Merupakan himpunan bagian dari B
print(A.issubset(B))
# 4. Apakah himpunan lepas A dan B
print(A.isdisjoint(B))
#5. Gabungkan A dengan B dan B dengan A

A.update(B)
print(A)

B.update(A)
print(B)

#6. Berapakah selisih simetris antara A dan B
selisih = A.difference(B)
print(selisih)

#7 hapus set 

A.clear()
B.clear()
print(A)
print(B)

# 1. Ubah umur menjadi suatu himpunan dan bandingkan panjang daftar dan himpunan tersebut, mana yang lebih besar?

age_set = set(age)
print(age_set)
print(len(age))
print(len(age_set))

kata = 'Saya seorang guru dan saya suka menginspirasi dan mengajar orang'
split_kata = kata.split()
print(split_kata)

kataset = set(split_kata)
print(kataset)

print(len(kataset))