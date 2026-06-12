language = 'Python'
lst = list(language)  # mengubah string menjadi daftar
print(type(lst))  # daftar
print(lst)

# Cara kedua: pemahaman daftar
lst = [i for i in language]
print(type(lst))  # daftar
print(lst)


numbers = [i for i in range(11)]
print(numbers)

# Operasi matematika dapat dilakukan selama iterasi
squares = [i * i for i in range(11)]
print(squares)

# Dimungkinkan juga untuk membuat daftar tupel
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Pemahaman daftar dapat dikombinasikan dengan ekspresi if

# ```python
# Menghasilkan bilangan genap
even_numbers = [i for i in range(21) if i % 2 == 0]  # untuk menghasilkan daftar bilangan genap dalam rentang 0 hingga 21
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Menghasilkan angka ganjil
odd_numbers = [i for i in range(21) if i % 2 != 0]  # untuk menghasilkan angka ganjil dalam rentang 0 hingga 21
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter angka: mari kita filter angka genap positif dari daftar di bawah
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)    

# Meratakan array dua dimensi
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


## Fungsi Lambda

# Fungsi Lambda adalah fungsi anonim kecil tanpa nama.Ini dapat mengambil sejumlah argumen, namun hanya dapat memiliki satu ekspresi.Fungsi Lambda mirip dengan fungsi anonim di JavaScript.Kita membutuhkannya ketika kita ingin menulis fungsi anonim di dalam fungsi lain.

### Membuat Fungsi Lambda

# Untuk membuat fungsi lambda kita menggunakan kata kunci _lambda_ diikuti dengan parameter, diikuti dengan ekspresi.Lihat sintaks dan contoh di bawah ini.Fungsi Lambda tidak menggunakan return tetapi secara eksplisit mengembalikan ekspresi.

# # sintaksis

# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

# **Contoh:**

# ```python
# Fungsi bernama
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))  # 5
# Mari kita ubah fungsi di atas menjadi fungsi lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))




def power(x):
    return lambda n : x ** n
# didalam fungsi ada lambda
cube = power(2)(3)  # fungsi power sekarang memerlukan 2 argumen untuk dijalankan, dalam tanda kurung bulat yang terpisah
print(cube)  # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

numbers = [(i, i * i) for i in range(11)]
print(numbers)