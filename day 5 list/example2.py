## Daftar

# Ada empat tipe data koleksi di Python:

# - Daftar : merupakan kumpulan yang urut dan dapat diubah-ubah.Mengizinkan anggota duplikat.
# - Tuple : merupakan kumpulan yang tertata dan tidak dapat diubah atau tidak dapat diubah.Mengizinkan anggota duplikat.
# - Set: adalah koleksi yang tidak diurutkan, tidak diindeks, dan tidak dapat dimodifikasi, namun kita dapat menambahkan item baru ke dalam set tersebut.Anggota duplikat tidak diperbolehkan.
# - Kamus: merupakan kumpulan yang tidak berurutan, dapat diubah, dimodifikasi, dan diindeks.Tidak ada anggota duplikat.

empty_list = list()
print(len(empty_list))


empty_list = []  # ini adalah daftar kosong, tidak ada item dalam daftar
print(len(empty_list))  # 0

fruits = ['banana', 'orange', 'mango', 'lemon']  # daftar buah-buahan
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']  # daftar sayuran
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # daftar produk hewani
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']  # daftar teknologi web
countries = ['Indo', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# Cetak daftar dan panjangnya
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# - Daftar dapat memiliki item dengan tipe data berbeda
lst = ['Vincen', 250, True, {'country':'Indo', 'city':'jakarta'}]# daftar yang berisi tipe data berbeda

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # kami mengakses item pertama menggunakan indeksnya
print(first_fruit)  # pisang
second_fruit = fruits[1]
print(second_fruit)  # oranye
last_fruit = fruits[3]
print(last_fruit)  # jeruk nipis
# Indeks terakhir
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print('='*20)
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)  # pisang
print(last_fruit)  # jeruk nipis
print(second_last)  # buah mangga

print('='*20)

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  # barang1
print(second_item)  # barang2
print(third_item)  # barang3
print(rest)  # ['item4', 'item5']

print('='*20)
# Contoh Kedua tentang membongkar daftar
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

print('='*20)
# Contoh Ketiga tentang membongkar daftar
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Indo','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

