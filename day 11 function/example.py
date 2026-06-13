## Fungsi

# Sejauh ini kita telah melihat banyak fungsi bawaan Python.Di bagian ini, kita akan fokus pada fungsi khusus.Apa itu fungsi?Sebelum kita mulai membuat fungsi, mari kita pelajari apa itu fungsi dan mengapa kita membutuhkannya?

# ### Mendefinisikan Fungsi

# Fungsi adalah blok kode atau pernyataan pemrograman yang dapat digunakan kembali yang dirancang untuk melakukan tugas tertentu.Untuk mendefinisikan atau mendeklarasikan suatu fungsi, Python menyediakan kata kunci _def_.Berikut ini adalah sintaks untuk mendefinisikan suatu fungsi.Blok kode fungsi dijalankan hanya jika fungsi tersebut dipanggil atau dipanggil.

# ### Mendeklarasikan dan Memanggil Fungsi

# Saat kita membuat suatu fungsi, kita menyebutnya dengan mendeklarasikan suatu fungsi.Saat kami mulai menggunakannya, kami menyebutnya fungsi _calling_ atau _invoking_.Fungsi dapat dideklarasikan dengan atau tanpa parameter.


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name():
#     codes
#     codes
# # Memanggil suatu fungsi
# function_name()


### Fungsi tanpa Parameter

# Fungsi dapat dideklarasikan tanpa parameter.




def generate_full_name ():
    first_name = 'Vincen'
    last_name = 'Babi'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()  # memanggil suatu fungsi

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


### Fungsi Mengembalikan Nilai - Bagian 1

# Fungsi mengembalikan nilai menggunakan pernyataan _return_.Jika suatu fungsi tidak memiliki pernyataan pengembalian, ia mengembalikan Tidak Ada.Mari kita tulis ulang fungsi di atas menggunakan return.Mulai sekarang, kita mendapatkan nilai dari suatu fungsi ketika kita memanggil fungsi tersebut dan mencetaknya.


def generate_full_name ():
    first_name = 'Vincen'
    last_name = 'Babi'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())


### Fungsi dengan Parameter

# Dalam suatu fungsi kita dapat meneruskan tipe data yang berbeda: nomor, string, boolean, daftar, tuple, kamus, atau ditetapkan sebagai parameter.

# - Parameter Tunggal: Jika fungsi kita mengambil parameter, kita harus memanggil fungsi kita dengan argumen


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name(parameter):
#     codes
#     codes
# # Fungsi panggilan
# print(function_name(argument))





def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Vincen'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# - Dua Parameter: Suatu fungsi mungkin memiliki atau tidak memiliki parameter atau parameter.Suatu fungsi mungkin juga memiliki dua atau lebih parameter.Jika fungsi kita menggunakan parameter, kita harus memanggilnya dengan argumen.Mari kita periksa suatu fungsi dengan dua parameter:


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name(para1, para2):
#     codes
#     codes
# # Fungsi panggilan
# print(function_name(arg1, arg2))


# 


def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Vincen','Babi'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N'  # nilainya harus diubah menjadi string terlebih dahulu
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


### Melewati Argumen dengan Kunci dan Nilai

# Jika kita meneruskan argumen dengan kunci dan nilai, urutan argumen tidak menjadi masalah.


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name(para1, para2):
#     codes
#     codes
# # Fungsi panggilan
# print(function_name(para1 = 'John', para2 = 'Doe'))  # urutan argumen tidak menjadi masalah di sini


# 


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Vincen', lastname = 'Babi')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2))  # Urutan tidak masalah


### Fungsi Mengembalikan Nilai - Bagian 2

# Jika kita tidak mengembalikan nilai dengan suatu fungsi, maka fungsi kita mengembalikan _None_ secara default.Untuk mengembalikan nilai dengan fungsi kita menggunakan kata kunci _return_ diikuti dengan variabel yang kita kembalikan.Kita dapat mengembalikan tipe data apa pun dari suatu fungsi.

# - Mengembalikan string:
# 


def print_name(firstname):
    return firstname
print_name('Vincen')  # Asabene

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Vincen', lastname='Babi')


# - Mengembalikan nomor:

# 


def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))


# - Mengembalikan boolean:
# 


def is_even (n):
    if n % 2 == 0:
        return True  # return menghentikan eksekusi fungsi lebih lanjut, mirip dengan break
    return False
print(is_even(10))  # BENAR
print(is_even(7))  # PALSU


# - Mengembalikan daftar:
# 


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))


### Berfungsi dengan Parameter Default

# Terkadang kita meneruskan nilai default ke parameter, saat kita memanggil fungsi tersebut.Jika kita tidak memberikan argumen saat memanggil fungsi, nilai defaultnya akan digunakan.


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name(param = value):
#     codes
#     codes
# # Fungsi panggilan
# function_name()
# function_name(arg)





def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Vincen'))

def generate_full_name (first_name = 'Vincen', last_name = 'Babi'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N'  # nilainya harus diubah menjadi string terlebih dahulu
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100))  # 9,81 - gravitasi rata-rata di permukaan bumi
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))  # gravitasi di permukaan Bulan


### Jumlah Argumen yang Sewenang-wenang

# Jika kita tidak mengetahui jumlah argumen yang kita berikan ke fungsi kita, kita dapat membuat fungsi yang dapat menerima sejumlah argumen dengan menambahkan \* sebelum nama parameter.


# sintaksis
# Mendeklarasikan suatu fungsi
# def function_name(*args):
#     codes
#     codes
# # Fungsi panggilan
# function_name(param1, param2, param3,..)





def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num  # sama dengan total = total + angka
    return total
print(sum_all_nums(2, 3, 5))  # 10


### Jumlah Parameter Default dan Sewenang-wenang dalam Fungsi


def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Vincen','Brook','David','Eyob')

### Pembongkaran kamus

# You can call a function which has named arguments using a dictionary with matching key names. You do so using ``**``.


# Tentukan fungsi yang menggunakan dua argumen: 'nama' dan 'lokasi'
def greet(name, location):
# Cetak pesan ucapan menggunakan argumen yang disediakan
    print("Hi there", name, "how is the weather in", location)

# Panggil fungsi menggunakan argumen kata kunci
greet(name="Alice", location="New York")  
# Keluaran: Hai Alice, bagaimana cuaca di New York

# Buat kamus dengan kunci yang cocok dengan nama parameter fungsi
my_dict = {"name": "Alice", "location": "New York"}

# Panggil fungsi menggunakan kamus membongkar
greet(**my_dict)  
# Operator ** membongkar kamus, meneruskan pasangan nilai kuncinya
# sebagai argumen kata kunci untuk fungsi tersebut.
# Keluaran: Hai Alice, bagaimana cuaca di New York


### Jumlah Argumen yang Dinamakan Sewenang-wenang

# Anda juga dapat mendefinisikan suatu fungsi untuk menerima sejumlah argumen bernama.


def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)


# Umumnya hindari hal ini kecuali diperlukan karena akan mempersulit pemahaman fungsi yang diterima dan dilakukan.

### Fungsi sebagai Parameter Fungsi Lain


# Anda dapat meneruskan fungsi sebagai parameter
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))  # 9
