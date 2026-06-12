# ## Tupel

# Tuple adalah kumpulan tipe data berbeda yang terurut dan tidak dapat diubah.Tupel ditulis dengan tanda kurung bulat, .Setelah tupel dibuat, kita tidak dapat mengubah nilainya.Kita tidak dapat menggunakan metode tambah, sisipkan, hapus dalam sebuah Tuple karena tidak dapat dimodifikasi dan dapat diubah.Berbeda dengan list, tuple memiliki sedikit metode.Metode yang berhubungan dengan tupel:

# - tuple : untuk membuat tupel kosong
# - count: untuk menghitung jumlah item tertentu dalam sebuah tuple
# - indeks: untuk menemukan indeks item tertentu dalam sebuah Tuple
# - `+` operator: to join two or more tuples and to create a new tuple







# - Tupel kosong: Membuat tupel kosong
# sintaksis
empty_tuple = ()
# atau menggunakan konstruktor Tuple
empty_tuple = tuple()
# sintaksis
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(tpl))
### Mengakses Item Tuple

tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

### Mengiris tupel
#Kita dapat membagi sub-tupel dengan menentukan rentang indeks di mana memulai dan mengakhiri tupel, nilai yang dikembalikan akan berupa tupel baru dengan item yang ditentukan.

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]  # semua item
all_items = tpl[0:]  # semua item
middle_two_items = tpl[1:3]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]  # semua item
all_fruits= fruits[0:]  # semua item
print('********')
print(all_fruits)
orange_mango = fruits[1:3]  # tidak termasuk item di indeks 3
orange_to_the_rest = fruits[1:]


# Sintaksis
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]  # semua item
middle_two_items = tpl[-3:-1]  # tidak termasuk item pada indeks 3 (-1)



fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]  # semua item
orange_mango = fruits[-3:-1]  # tidak termasuk item di indeks 3
orange_to_the_rest = fruits[-3:]

### Mengubah Tupel menjadi Daftar

# Kita dapat mengubah tupel menjadi daftar dan daftar menjadi tupel.Tuple tidak dapat diubah jika kita ingin memodifikasi tuple kita harus mengubahnya menjadi daftar.


# Sintaksis
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)



fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)  # ['apel', 'jeruk', 'mangga', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apel', 'jeruk', 'mangga', 'lemon')


### Memeriksa Item di Tuple

# Kita dapat memeriksa apakah suatu item ada atau tidak dalam tupel menggunakan _in_, ia mengembalikan boolean.


# Sintaksis
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl  # BENAR



fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # BENAR
print('apple' in fruits)  # PALSU
# fruits[0] = 'apple'  # TypeError: objek 'tuple' tidak mendukung penetapan item


### Bergabung dengan Tuple

# Kita dapat menggabungkan dua tupel atau lebih menggunakan operator +


# sintaksis
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2



fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables


### Menghapus Tuple

# Tidak mungkin untuk menghapus satu item pun dalam sebuah tupel tetapi dimungkinkan untuk menghapus tupel itu sendiri menggunakan _del_.

# sintaksis
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits