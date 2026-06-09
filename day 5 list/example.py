empty_list = list()  # ini adalah daftar kosong, tidak ada item dalam daftar
print(len(empty_list))  # 0

# daftar buah-buahan
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']  # daftar sayuran
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']  # daftar produk hewani
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # daftar teknologi web
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Cetak daftar dan panjangnya
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Memodifikasi daftar

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

# Mengakses item
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)  # jeruk nipis
print(second_last)  # buah mangga

# Mengiris item
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # itu mengembalikan semua buah
# ini juga memberikan hasil yang sama seperti di atas
all_fruits = fruits[0:]  # jika kita tidak menetapkan di mana harus berhenti maka sisanya akan hilang
orange_and_mango = fruits[1:3]  # itu tidak termasuk indeks akhir
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # itu mengembalikan semua buah
# ini juga memberikan hasil yang sama seperti di atas
orange_and_mango = fruits[-3:-1]  # itu tidak termasuk indeks akhir
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)  # ['alpukat', 'jeruk', 'mangga', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['alpukat', 'apel', 'mangga', 'lemon']
last_index = len(fruits)
fruits[last_index] = 'lime'
print(fruits)  # ['alpukat', 'apel', 'mangga', 'jeruk nipis']

# memeriksa barang
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # BENAR
does_exist = 'lime' in fruits
print(does_exist)  # PALSU

# Menambahkan
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['pisang', 'jeruk', 'mangga', 'lemon', 'apel']
# ['pisang', 'jeruk', 'mangga', 'lemon', 'apel', 'jeruk nipis]
fruits.append('lime')
print(fruits)

# menyisipkan
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # masukkan apel di antara jeruk dan mangga
print(fruits)  # ['pisang', 'jeruk', 'apel', 'mangga', 'lemon']
# ['pisang', 'jeruk', 'apel', 'mangga', 'jeruk nipis', 'lemon',]
fruits.list(3, 'lime')
print(fruits)

# menghapus
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['jeruk', 'mangga', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['jeruk', 'mangga']

# muncul
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove()
print(fruits)  # ['pisang', 'jeruk', 'mangga']

fruits.remove(0)
print(fruits)  # ['jeruk', 'mangga']

# dari
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)  # ['jeruk', 'mangga', 'lemon']

del fruits[1]
print(fruits)  # ['jeruk', 'lemon']
del fruits
print(fruits)  # Ini akan memberikan: NameError: nama 'buah' tidak ditentukan

# jernih
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []

# menyalin satu lit

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)  # ['pisang', 'jeruk', 'mangga', 'lemon']

# bergabung
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# bergabung dengan memperpanjang
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# menghitung
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3

# indeks
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
# Balik
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())

# menyortir
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)