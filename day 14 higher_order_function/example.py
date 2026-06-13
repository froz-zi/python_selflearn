def sum_numbers(nums):  # fungsi normal
    return sum(nums)  # fungsi menyedihkan yang menyalahgunakan fungsi penjumlahan bawaan :<

def higher_order_function(f, lst):  # berfungsi sebagai parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15



### Berfungsi sebagai Nilai Pengembalian


def square(x):  # fungsi persegi
    return x ** 2

def cube(x):  # fungsi kubus
    return x ** 3

def absolute(x):  # fungsi nilai absolut
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):  # fungsi tingkat tinggi yang mengembalikan suatu fungsi
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))  # 9
result = higher_order_function('cube')  
print(result(3))  # 27
result = higher_order_function('absolute')
print(result(-3))  # 3


## Penutupan Python

# Python mengizinkan fungsi bersarang untuk mengakses cakupan luar dari fungsi terlampir.Ini dikenal sebagai Penutupan.Mari kita lihat cara kerja penutupan dengan Python.Di Python, penutupan dibuat dengan menyarangkan fungsi di dalam fungsi enkapsulasi lain dan kemudian mengembalikan fungsi bagian dalam.Lihat contoh di bawah ini.


def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


## Dekorator Python

# Dekorator adalah pola desain dengan Python yang memungkinkan pengguna menambahkan fungsionalitas baru ke objek yang sudah ada tanpa mengubah strukturnya.Dekorator biasanya dipanggil sebelum definisi fungsi yang ingin Anda hias.

# ### Membuat Dekorator

# Untuk membuat fungsi dekorator, kita memerlukan fungsi luar dengan fungsi pembungkus dalam.

# **Contoh:**

# ```python
# Fungsi biasa
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())  # SELAMAT DATANG DI PYTHON

#  Mari kita terapkan contoh di atas dengan dekorator

# '''This decorator function is a higher order function
# that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())


### Menerapkan Beberapa Dekorator ke Satu Fungsi


# ### Menerapkan Beberapa Dekorator ke Satu Fungsi
# ```python

# '''These decorator functions are higher order functions
# that take functions as parameters'''

# Dekorator Pertama
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Dekorator kedua
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# Dekorator akan dieksekusi dari bawah ke atas
# @split_string_decorator
# @uppercase_decorator  # urutan dengan dekorator penting dalam hal ini - fungsi .upper() tidak berfungsi dengan daftar
def greeting():
    return 'Welcome to Python'
print(greeting())  # ['SELAMAT DATANG', 'KEPADA', 'PYTHON']

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters
# @decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')


## Fungsi Tingkat Tinggi Bawaan

# Beberapa fungsi tingkat tinggi bawaan yang kita bahas di bagian ini adalah _map_, _filter_, dan _reduce_.
# Fungsi Lambda dapat diteruskan sebagai parameter dan kasus penggunaan terbaik dari fungsi lambda ada pada fungsi seperti peta, filter, dan pengurangan.

### Python - Fungsi Peta

# Fungsi peta adalah fungsi bawaan yang menggunakan suatu fungsi dan dapat diubah sebagai parameter.

# ```python
# sintaksis
#     map(function, iterable)
# ```

# **Contoh:1**

# ```python
numbers = [1, 2, 3, 4, 5]  # dapat diubah
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# Mari kita terapkan dengan fungsi lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# ```

# **Contoh:2**

# ```python
numbers_str = ['1', '2', '3', '4', '5']  # dapat diubah
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]
# ```

# **Contoh:3**

# ```python
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # dapat diubah

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # [Asabnahi, Al-Diyaa, Armasi, kuburan mereka]